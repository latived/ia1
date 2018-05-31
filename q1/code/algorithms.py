# -*- coding: utf-8 -*-
from .checks import check_state

# In hourly-order from the right.
valid_moves = {0: [1, 3],
               1: [2, 4, 0],
               2: [5, 1],
               3: [4, 6, 0],
               4: [5, 7, 3, 1],
               5: [8, 4, 2],
               6: [7, 3],
               7: [8, 6, 4],
               8: [7, 5]}


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


def search(state, search_type="bfs"):
    if search_type not in ["bfs", "dfs"]: 
        print("[error] algorithm not found: ", search_type)
        return False
   
    state = (state, None, 0)
    open_states = [state]  # modified to know path taken
    closed_states = []
    reps = -1  # depth began at value 0
    
    while len(open_states) != 0:
        reps += 1
        cs = open_states[0]  # current state
        open_states.remove(cs)
        
        if check_state(cs[0]):  # modified
            print("[", search_type, "] a solution was found!")
            print("[", search_type, "] total of iterations: ", reps)
            print("[", search_type, "] solutions' depth: ", cs[2])
            return True
        else:
            closed_states.append(cs)
    
            # gen_children now returns (state, cs, length_par+1)
            cs_children = gen_children(cs) 
            for child in cs_children.copy():
                if child in open_states:
                    cs_children.remove(child)
                if child in closed_states:
                    cs_children.remove(child)
            if search_type == "dfs":
                open_states = cs_children + open_states
            else:
                open_states.extend(cs_children)
    print("[", search_type, "] solution not found.")
    print("[", search_type, "] total of iterations: ", reps)
    return False


def iddfs(state, limit, tx):
    state = (state, None, 0) 
    tx_temp = tx
    print("[iddfs] used limit: ", limit)
    print("[iddfs] growth rate: ", tx)
    # TODO: save where it stops after limit has been reached (to not start over again)
    for depth in range(0, tx_temp):
        found = dls(state, depth)
        if found:
            print("[iddfs] a solution was found!")
            return found
    if tx_temp <= limit:
        tx_temp += tx
    else:
        print("[iddfs] limit reached... exiting...")


def dls(state, depth):
    if depth == 0 and check_state(state[0]):
        # TODO: changes in tx_temp
        print("[iddfs] depth of solution: ", state[2])
        return True 
    if depth > 0:
        for child in gen_children(state):
            found = dls(child, depth-1)
            if found:
                return found

    return False