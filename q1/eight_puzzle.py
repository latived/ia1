#!/usr/bin/env python3

import time
import threading

from algorithms import search
from algorithms import IDDFS
from algorithms import DLS
from algorithms import gen_children

from checks import check_solvable
from checks import check_is_state_valid

def call_bfs(state):
    print("\n########### usando bfs #######################")
    start = time.time()
    search(state) # bfs default
    end = time.time()
    print("Tempo total: ", end - start)

def call_dfs(state):
    print("\n########### usando dfs #######################")
    start = time.time()
    search(state, "dfs")
    end = time.time()
    print("Tempo total: ", end - start)

def call_iddfs(state, limit, tx):
    print("\n########### usando idfs ######################")
    start = time.time()
    IDDFS(state, 10000, 1000)
    end = time.time()
    print("Tempo total: ", end - start)


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
        limit = 10000 # for iddfs
        tx    = 1000  # for iddfs
        
        tbfs = threading.Thread(name='bfs', target=search, args=(start_state,'dfs'))
        tdfs = threading.Thread(name='dfs', target=search, args=(start_state,))
        tiddfs = threading.Thread(name='iddfs', target=IDDFS,
                args=(start_state, limit, tx))

        tbfs.start()
        tdfs.start()
        tiddfs.start()


if __name__ == "__main__":
     main()
 
