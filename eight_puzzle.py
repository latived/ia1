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

def check(state):
    for i in range(9):
        if i+1 != state[i]:
            return false
    return true


def move(state, direction):
    blank_zero = state.index(0)
    valid_for_dir = valid_moves[blank_zero]
    if (direction in valid_for_dir):
        state[blank_zero], state[direction]= state[direction], 0
    else:
        print("Invalid move!")
