#!/usr/bin/env python3

valid_moves = {0 : [1,3],
               1 : [0,2,4],
               2 : [1,5],
               3 : [0,4,6],
               4 : [1,3,5,7],
               5 : [2,8,4],
               6 : [3,7],
               7 : [4,8,6],
               8 : [5,7]}

def check_state(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    #goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    return state == goal_state

def show_states_conf(state):
    print("\t{0} {1} {2}\n\t{3} {4} {5}\n\t{6} {7} {8}\n".format(
        state[0], state[1], state[2],
        state[3], state[4], state[5],
        state[6], state[7], state[8]
        )
        )

def iterative(state):
    print("Não implementado.")

def gen_children(state):
    idx_zero = state.index(0)
    moves = valid_moves[idx_zero]
    children = []
    for move in moves:
        new_state = state.copy()
        new_state[move], new_state[idx_zero] = 0, state[move]
        children.append(new_state)
    return children

def search(state, search_type = "bfs"):
    if search_type not in ["bfs", "dfs"]: 
        print("Algoritmo inexistente: ", search_type)
        return False
    # TODO: add (state, parent, length)
    init_state = state.copy()
    open_states = [state]
    closed_states = []
    reps = 0
    depth_bound = 5
    while len(open_states) != 0 and (search_type == "bfs" or reps <= 
            depth_bound):
        reps += 1
        cs = open_states[0] # current state
        open_states.remove(cs)
        if check_state(cs): 
            print("\tSolucionado! Caminho... ainda não disponível!")
            print("State 0: ")
            show_states_conf(init_state)
            print("Final state: ")
            show_states_conf(cs)
            print("Final lvl: ", reps-1)
            return True
        else:
            print("Lvl ", reps)
            print("State: ")
            show_states_conf(cs)
            
            cs_children = gen_children(cs)
            
            print("Children possible: ")
            for c in cs_children: show_states_conf(c)
            
            closed_states.append(cs)
            
            print("Children selected: ")
            
            for child in cs_children:
                if (child not in open_states) and (child not in closed_states):
                    show_states_conf(child)
                else:
                    cs_children.remove(child)
            if search_type == "dfs":
                open_states = cs_children + open_states
            else:
                open_states.extend(cs_children)
    print("Solução não encontrada.")
    return False

# IDDFS
def IDDFS(state, limit):
    for depth in range(0, limit):
        print("#########################")
        print("Began at limit ", depth)
        print("Lvl ", depth)
        found = DLS(state, depth)
        if found:
            return found
        else:
            print("bad limit. nothing here. next limit...")

def DLS(state, depth):
    print("actual: ")
    show_states_conf(state)
    # with and we get more
    if depth == 0 and check_state(state):
        print("found it.")
        return True 
    if depth > 0:
        for child in gen_children(state):
            show_states_conf(child)
            print("deepening more...")
            found = DLS(child, depth-1)
            print("next child...? ")
            if found:
                print(" not really.")
                return found

    print("hitting bottom. nothing here. going back...")
    return False



def main():
    #state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
    print("Lvl 0")
    show_states_conf(state)
    print("Com DFS: ")
    search(state, "dfs")
    print("##################################")
    print("Com BFS: ")
    search(state) # bfs default
 
if __name__ == "__main__":
     main()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
