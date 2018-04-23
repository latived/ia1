
from checks import check_state

# em ordem horária a partir da direita
valid_moves = {0 : [1,3],
               1 : [2,4,0],
               2 : [5,1],
               3 : [4,6,0],
               4 : [5,7,3,1],
               5 : [8,4,2],
               6 : [7,3],
               7 : [8,6,4],
               8 : [7,5]}

def gen_children(state):
    idx_zero = state[0].index(0)
    moves = valid_moves[idx_zero]
    children = []
    for move in moves:
        new_state = state[0].copy()
        new_state[move], new_state[idx_zero] = 0, state[0][move]
        new_state = (new_state, state[0], state[2]+1)
        children.append(new_state)
    return children

def search(state, search_type = "bfs"):
    if search_type not in ["bfs", "dfs"]: 
        print("Algoritmo inexistente: ", search_type)
        return False
   
    state = (state, None, 0)
    open_states = [state] # modified to know path taken
    closed_states = []
    reps = -1 # depth began at value 0
    
    while len(open_states) != 0:
        reps += 1
        cs = open_states[0] # current state
        open_states.remove(cs)
        
        if check_state(cs[0]): # modified
            print("Solução encontrada!")
            print("Total de iterações: ", reps)
            print("Profundidade da solução: ", cs[2])
            return True
        else:
            closed_states.append(cs)
    
            # gen_children now returns (state, cs, lengh_par+1)
            cs_children = gen_children(cs) 
            for child in cs_children.copy():
                if (child in open_states):
                    cs_children.remove(child)
                if (child in closed_states):
                    cs_children.remove(child)
            if search_type == "dfs":
                open_states = cs_children + open_states
            else:
                open_states.extend(cs_children)
    print("Solução não encontrada.")
    print("Total de iterações: ", reps)
    return False

# IDDFS
def IDDFS(state, limit, tx):
    state = (state, None, 0) 
    tx_temp = tx
    print("Limite usado: ", limit)
    print("Taxa de crescimento: ", tx)
    for depth in range(0, tx_temp):
        found = DLS(state, depth)
        if found:
            print("Solução encontrada!")
            return found
    if tx_temp <= limit:
        tx_temp += tx
    else:
        print("Limite alcançado... saindo...")

def DLS(state, depth):
    if depth == 0 and check_state(state[0]):
        print("Profundidade da solução: ", state[2]) # TODO: mudanças em tx_temp
        return True 
    if depth > 0:
        for child in gen_children(state):
            found = DLS(child, depth-1)
            if found:
                return found

    return False
