import unittest

from ..code import algorithms
from .mockutils import get_tuple_mock
from .mockutils import populate_states


class AlgorithmsTest(unittest.TestCase):

    def test_remove_marked_children(self):

        # Check children simply sees if an state is in either open or closed_states list.
        # A child is a ordinary state tuple (state, parent, depth)
        # To test check_children, it's doesn't really matter what a 'child' is.
        # In fact, check_children will do with any list of objects.

        open_states = []    # A list of states tuples (state, parent, depth) not marked
        closed_states = []  # A list of states tuples already marked as seen

        mock_inside_open = get_tuple_mock()
        mock_inside_closed = get_tuple_mock()
        mock_outside_any = get_tuple_mock()

        open_states.append(mock_inside_open)
        closed_states.append(mock_inside_closed)

        children = [mock_inside_open,
                    mock_inside_closed,
                    mock_outside_any]

        populate_states(50, open_states)
        populate_states(70, closed_states)

        algorithms.remove_marked_children(children,
                                          open_states,
                                          closed_states)

        self.assertEqual(children, [mock_outside_any])

    def test_gen_children_move_from_0(self):
        # Simple, for now.
        state_with_0_at_0 = ([0, 1, 2,
                             3, 4, 5,
                             6, 7, 8], None, 0)

        children_from_0 = [([1, 0, 2,
                            3, 4, 5,
                            6, 7, 8], state_with_0_at_0[0], 1),
                           ([3, 1, 2,
                            0, 4, 5,
                            6, 7, 8], state_with_0_at_0[0], 1)]

        # TODO: how to test this in a more generic way?

        self.assertEqual(algorithms.gen_children(state_with_0_at_0), children_from_0)

    # TODO: test for 0 in 1-8 positions
    def test_search_dfs(self):
        pass

    def test_search_bfs(self):
        pass

    def test_search_iddfs(self):
        pass


if __name__ == '__main__':
    unittest.main()
