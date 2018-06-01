from unittest.mock import Mock


def get_tuple_mock():
    return tuple([Mock(), Mock(), Mock()])


def populate_states(n, states):
    for _ in range(n):
        states.append(get_tuple_mock())
