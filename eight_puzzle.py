#!/usr/bin/env python3

# state space is the range of configurations we can reach when we apply
# procedures, that is, we move the blank space 
# (NOTE: moves are four = up, right, down, left;
# but procedures are limited by parameters/actual configuration)
#
# state space for this puzzle is a graph
#
# state can be a simple 3x3 array
#
# beginning state: anything?
#   1 4 3       _ 8 1
#   7 _ 6   or  2 7 3 or ... 
#   5 8 2       4 6 5
# 
# goal state: 
#   1 2 3
#   4 5 6
#   7 8 _
#
# to list both beginning and goal states have the form:
#   bs: 1 4 3 7 0 6 5 8 2 or 0 8 1 2 7 3 4 6 5 or ...
#   gs: 1 2 3 4 5 6 7 8 0
#
# in this case, a valid move would be, from a certain pos (1-9):
# 1 -> 2,4
# 2 -> 1,3,5
# 3 -> 2,6
# 4 -> 1,5,7
# 5 -> 2,4,6,8
# 6 -> 3,5,9
# 7 -> 4,8
# 8 -> 5,7,9
# 9 -> 6,8
#
# parameters: 9, location of numbers in the grid

valid_moves = {1 : [2,4],
               2 : [1,3,5],
               3 : [2,6],
               4 : [1,5,7],
               5 : [2,4,6,8],
               6 : [3,5,9],
               7 : [4,8],
               8 : [5,7,9],
               9 : [6,8]}

def check_state(state):
    for i in range(8):
        if i+1 != state[i]:
            return False
    if state[8] != 0: return False
    return True

def iterativo(state):
    print("Não implementado.")

# na solução poderá aparecer mais de um caminho válido
moves = []
def dfs(state):
    if check_state(state):
        print("Solucionado! {}".format(state))
        print("Estados procurados, total: {}".format(len(moves)))
    else:
        # Here we do pos_zero + 1 because in valid_moves
        # we have the positions from 1 to 9
        pos_zero = state.index(0) 
        for d in valid_moves[pos_zero + 1]:
            temp_state = state.copy()
            # Same here: d is in [1,9], so we have to subtract 1
            temp_state[pos_zero], temp_state[d-1]= temp_state[d-1], 0
            if [pos_zero, d-1] not in moves or [d-1, pos_zero] not in moves: 
                print("{0} to {1}".format(pos_zero+1, d))
                moves.append([pos_zero, d-1])
                dfs(temp_state)


def main():
    state = [1, 2, 3, 4, 5, 6, 7, 0, 8]
    print("Initial state: {}".format(state))
    dfs(state)

if __name__ == "__main__":
    main()
