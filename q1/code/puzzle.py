# -*- coding: utf-8 -*-
import sys
import time
import threading

from .algorithms import search
from .algorithms import iddfs

from .checks import check_solvable
from .checks import check_is_state_valid


def call_bfs(state):
    print("[info] bfs running...")
    start = time.time()
    search(state)  # bfs default
    end = time.time()
    print("[ bfs ] tempo total: ", end - start)


def call_dfs(state):
    print("[info] dfs running...")
    start = time.time()
    search(state, "dfs")
    end = time.time()
    print("[ dfs ] total time: ", end - start)


def call_iddfs(state, limit, tx):
    print("[info] iddfs running...")
    start = time.time()
    iddfs(state, limit, tx)
    end = time.time()
    print("[iddfs] tempo total: ", end - start)


def main():
    print("---------- 8-PUZZLE GAME ----------")
    print("Type 'exit' to get out.")
    b = threading.Barrier(3)
    while True:
        start_state = input("> ")

        if start_state == "exit":
            print("Exiting...")
            sys.exit()

        try:
            start_state = list(map(int, start_state.split()))
        except ValueError:
            print("Wrong input! You need to type 9 digits from 0 to 8,"
                  " separated by spaces.")
            continue

        goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

        if start_state == goal_state:
            print("Input state is already solved.")
            continue

        if check_is_state_valid(start_state) and check_solvable(start_state):
            print("---------- 8-PUZZLE GAME: running ----------")
            print("[info] initial state: ", start_state)
            print("[info] final state  : ", goal_state)

            limit = 10000  # for iddfs
            tx = 1000      # for iddfs

            tbfs = threading.Thread(name='bfs',
                                    target=call_bfs,
                                    args=(start_state,))

            tdfs = threading.Thread(name='dfs',
                                    target=call_dfs,
                                    args=(start_state,))

            tiddfs = threading.Thread(name='iddfs',
                                      target=call_iddfs,
                                      args=(start_state, limit, tx))

            tbfs.start()
            tdfs.start()
            tiddfs.start()

            b.wait()  # wait for the threads above terminate.
