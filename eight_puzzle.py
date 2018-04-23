#!/usr/bin/env python3

import time

# 0 1 2
# 3 4 5
# 6 7 8

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

def check_solvable(state):
    acc = 0
    temp_state = state[:]
    temp_state.remove(0)
    for n1 in range(len(temp_state)):
        for n2 in range(n1, len(temp_state)):
            if temp_state[n1] > temp_state[n2]: acc += 1

    if acc % 2 == 1:
        print("Configuração impossível de ser solucionada!")
        return False
    else:
        print("Solucionável! Pode tentar.")
        return True

def check_state(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return state == goal_state

def show_states_conf(state):
    print("\t{0} {1} {2}\n\t{3} {4} {5}\n\t{6} {7} {8}\n".format(
        state[0], state[1], state[2],
        state[3], state[4], state[5],
        state[6], state[7], state[8]
        )
        )

# modified to get path taken
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

# TODO: add hash to see if state has been visited instead of list
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

def check_is_state_valid(state):
    if len(state) != 9:
        print("Estado inválido: tamanho {} não permitido.".format(len(state)))
        return False
    for i in range(9):
        if i not in state:
            print("Estado inválido: pelo menos um valor no intervalo (0-8) faltando.")
            return False
    return True

def main():
    #state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    #state = [1, 2, 3, 4, 5, 6, 8, 7, 0]
    #state = [2, 4, 0, 8, 5, 3, 1, 7, 6]
    #state = [8,6,7,2,5,4,3,0,1]
    start_state = input("> ")
    start_state = list(map(int, start_state.split()))
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if check_is_state_valid(start_state) and check_solvable(start_state):

        print("Estado inicial: ", start_state)
        print("Estado final  : ", goal_state)
        print("\n########### usando bfs #######################")
        start = time.time()
        search(start_state) # bfs default
        end = time.time()
        print("Tempo total: ", end - start)
        print("\n########### usando dfs #######################")
        start = time.time()
        search(start_state, "dfs")
        end = time.time()
        print("Tempo total: ", end - start)
        print("\n########### usando idfs ######################")
        start = time.time()
        IDDFS(start_state, 10000, 1000)
        end = time.time()
        print("Tempo total: ", end - start)
    
if __name__ == "__main__":
     main()
 
