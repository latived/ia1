def show_states_conf(state):
    print("\t{0} {1} {2}\n\t{3} {4} {5}\n\t{6} {7} {8}\n".format(
        state[0], state[1], state[2],
        state[3], state[4], state[5],
        state[6], state[7], state[8])
    )


def check_solvable(state):
    acc = 0
    temp_state = state[:]
    temp_state.remove(0)
    for n1 in range(len(temp_state)):
        for n2 in range(n1, len(temp_state)):
            if temp_state[n1] > temp_state[n2]:
                acc += 1

    if acc % 2 == 1:
        print("[error] this configuration can not be solved!")
        return False
    else:
        print("[info] it can be solved, try it!")
        return True


def check_state(state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    return state == goal_state


def check_is_state_valid(state):
    if len(state) != 9:
        print("[error] invalid config: size {} not permitted.".format(len(state)))
        return False
    for i in range(9):
        if i not in state:
            print("[error] invalid config: at least one value in (0-8) interval missing.")
            return False
    return True


def check_input_ok(start_state, goal_state):
    try:
        start_state = list(map(int, start_state.split()))
    except ValueError:
        print("[error] you need to type 9 digits from 0 to 8,"
              " separated by spaces.")
        return False

    if start_state == goal_state:
        print("[info] input state is already solved.")
        return False

    return True
