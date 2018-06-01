from unittest.mock import Mock


def get_tuple_mock():
    return tuple([Mock(), Mock(), Mock()])


def get_list_mocks(idx=None):
    mocks = [Mock() for _ in range(9)]
    mocks[idx] = 0
    return mocks


def populate_states(n, states):
    for _ in range(n):
        states.append(get_tuple_mock())
