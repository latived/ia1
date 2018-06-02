import random
import unittest

from ..code import checks
from ..code import algorithms

from ..code.exceptions import UnsolvableConfigurationError

from .mockutils import get_tuple_mock
from .mockutils import populate_states
from .mockutils import get_list_mocks



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

    # Testing a private method.
    # Because Python uses access modifiers by convention,
    # we don't have 'reflection' as in Java.
    def test_swap_0_from_1(self):
        state_1 = get_list_mocks(1)
        state_2 = algorithms._swap_0(state_1, 1, 2)
        state_4 = algorithms._swap_0(state_1, 1, 4)
        state_0 = algorithms._swap_0(state_1, 1, 0)

        # Asserting that 0 is in the right position
        self.assertEqual(state_2[2], 0)
        self.assertEqual(state_4[4], 0)
        self.assertEqual(state_0[0], 0)

        # Asserting that if I undo the swap, we go back to state_1
        self.assertEqual(algorithms._swap_0(state_2, 2, 1), state_1)
        self.assertEqual(algorithms._swap_0(state_4, 4, 1), state_1)
        self.assertEqual(algorithms._swap_0(state_0, 0, 1), state_1)

        # As you can see, testing fro 1, 4, and 7 we have tested for all positions.

    def test_swap_0_from_4(self):
        state_4 = get_list_mocks(4)
        state_5 = algorithms._swap_0(state_4, 4, 5)
        state_7 = algorithms._swap_0(state_4, 4, 7)
        state_3 = algorithms._swap_0(state_4, 4, 3)
        state_1 = algorithms._swap_0(state_4, 4, 1)

        # Asserting that 0 is in the right position
        self.assertEqual(state_5[5], 0)
        self.assertEqual(state_7[7], 0)
        self.assertEqual(state_3[3], 0)
        self.assertEqual(state_1[1], 0)

        # Asserting that if I undo the swap, we go back to state_4
        self.assertEqual(algorithms._swap_0(state_5, 5, 4), state_4)
        self.assertEqual(algorithms._swap_0(state_7, 7, 4), state_4)
        self.assertEqual(algorithms._swap_0(state_3, 3, 4), state_4)
        self.assertEqual(algorithms._swap_0(state_1, 1, 4), state_4)

    def test_swap_0_from_7(self):
        state_7 = get_list_mocks(7)
        state_8 = algorithms._swap_0(state_7, 7, 8)
        state_6 = algorithms._swap_0(state_7, 7, 6)
        state_4 = algorithms._swap_0(state_7, 7, 4)

        # Asserting that 0 is in the right position
        self.assertEqual(state_8[8], 0)
        self.assertEqual(state_6[6], 0)
        self.assertEqual(state_4[4], 0)

        # Asserting that if I undo the swap, we go back to state_7
        self.assertEqual(algorithms._swap_0(state_8, 8, 7), state_7)
        self.assertEqual(algorithms._swap_0(state_6, 6, 7), state_7)
        self.assertEqual(algorithms._swap_0(state_4, 4, 7), state_7)

    def test_gen_children_move_from_0(self):
        # In gen_children method we only look for the 0's position
        # Any other number isn't evaluated, therefore we can Mock the rest of fit.
        # Like: state = [Mocks ... 0] or [Mocks ... 0 ... Mocks] or [0 ... Mocks]

        # get_list_mocks(idx) return a list of mocks but with 0 in idx position
        state_0 = get_list_mocks(0)
        state_1 = algorithms._swap_0(state_0, 0, 1)
        state_3 = algorithms._swap_0(state_0, 0, 3)

        state_with_0_at_0 = (state_0,
                             None,
                             0)

        children_from_0 = [(state_1,
                            state_0,
                            1),
                           (state_3,
                            state_0,
                            1)]

        self.assertEqual(algorithms.gen_children(state_with_0_at_0), children_from_0)

    def test_gen_children_move_from_1(self):
        state_1 = get_list_mocks(1)
        state_2 = algorithms._swap_0(state_1, 1, 2)
        state_4 = algorithms._swap_0(state_1, 1, 4)
        state_0 = algorithms._swap_0(state_1, 1, 0)

        state_with_0_at_1 = (state_1,
                             None,
                             0)

        children_from_1 = [(state_2,
                            state_1,
                            1),
                           (state_4,
                            state_1,
                            1),
                           (state_0,
                            state_1,
                            1)]

        self.assertEqual(algorithms.gen_children(state_with_0_at_1), children_from_1)

    def test_gen_children_move_from_2(self):
        state_2 = get_list_mocks(2)
        state_5 = algorithms._swap_0(state_2, 2, 5)
        state_1 = algorithms._swap_0(state_2, 2, 1)

        state_with_0_at_2 = (state_2,
                             None,
                             0)

        children_from_2 = [(state_5,
                            state_2,
                            1),
                           (state_1,
                            state_2,
                            1)]

        self.assertEqual(algorithms.gen_children(state_with_0_at_2), children_from_2)

    def test_gen_children_move_from_3(self):
        state_parent = get_list_mocks(3)
        state_child = [None, None, None]
        state_child[0] = algorithms._swap_0(state_parent, 3, 4)
        state_child[1] = algorithms._swap_0(state_parent, 3, 6)
        state_child[2] = algorithms._swap_0(state_parent, 3, 0)

        state_parent_tuple = (state_parent,
                              None,
                              0)

        children_from_3 = [(state_child[0],
                            state_parent,
                            1),
                           (state_child[1],
                            state_parent,
                            1),
                           (state_child[2],
                            state_parent,
                            1)]

        self.assertEqual(algorithms.gen_children(state_parent_tuple), children_from_3)

    def test_gen_children_move_from_4(self):
        state_parent = get_list_mocks(4)
        state_child = [None, None, None, None]
        state_child[0] = algorithms._swap_0(state_parent, 4, 5)
        state_child[1] = algorithms._swap_0(state_parent, 4, 7)
        state_child[2] = algorithms._swap_0(state_parent, 4, 3)
        state_child[3] = algorithms._swap_0(state_parent, 4, 1)

        state_parent_tuple = (state_parent,
                              None,
                              0)

        children = [(state_child[0],
                     state_parent,
                     1),
                    (state_child[1],
                     state_parent,
                     1),
                    (state_child[2],
                     state_parent,
                     1),
                    (state_child[3],
                     state_parent,
                     1)]

        self.assertEqual(algorithms.gen_children(state_parent_tuple), children)

    def test_gen_children_move_from_5(self):
        state_parent = get_list_mocks(5)
        state_child = [None, None, None, None]
        state_child[0] = algorithms._swap_0(state_parent, 5, 8)
        state_child[1] = algorithms._swap_0(state_parent, 5, 4)
        state_child[2] = algorithms._swap_0(state_parent, 5, 2)

        state_parent_tuple = (state_parent,
                              None,
                              0)

        children = [(state_child[0],
                     state_parent,
                     1),
                    (state_child[1],
                     state_parent,
                     1),
                    (state_child[2],
                     state_parent,
                     1)]

        self.assertEqual(algorithms.gen_children(state_parent_tuple), children)

    def test_gen_children_move_from_6(self):
        state_parent = get_list_mocks(6)
        state_child = [None, None, None, None]
        state_child[0] = algorithms._swap_0(state_parent, 6, 7)
        state_child[1] = algorithms._swap_0(state_parent, 6, 3)

        state_parent_tuple = (state_parent,
                              None,
                              0)

        children = [(state_child[0],
                     state_parent,
                     1),
                    (state_child[1],
                     state_parent,
                     1)]

        self.assertEqual(algorithms.gen_children(state_parent_tuple), children)

    def test_gen_children_move_from_7(self):
        state_parent = get_list_mocks(7)
        state_child = [None, None, None, None]
        state_child[0] = algorithms._swap_0(state_parent, 7, 8)
        state_child[1] = algorithms._swap_0(state_parent, 7, 6)
        state_child[2] = algorithms._swap_0(state_parent, 7, 4)

        state_parent_tuple = (state_parent,
                              None,
                              0)

        children = [(state_child[0],
                     state_parent,
                     1),
                    (state_child[1],
                     state_parent,
                     1),
                    (state_child[2],
                     state_parent,
                     1)]

        self.assertEqual(algorithms.gen_children(state_parent_tuple), children)

    def test_gen_children_move_from_8(self):
        state_parent = get_list_mocks(8)
        state_child = [None, None]
        state_child[0] = algorithms._swap_0(state_parent, 8, 7)
        state_child[1] = algorithms._swap_0(state_parent, 8, 5)

        state_parent_tuple = (state_parent,
                              None,
                              0)

        children = [(state_child[0],
                     state_parent,
                     1),
                    (state_child[1],
                     state_parent,
                     1)]

        self.assertEqual(algorithms.gen_children(state_parent_tuple), children)

    def test_search_any(self):
        state = list(range(9))
        random.shuffle(state)
        self.assertFalse(algorithms.search(state, 'afs'))  # afs is not a algorithm

    """
    The only way I see to test the algorithms is by data and brute force.
    It can be time consuming.
    I haven't figured out a way to test check_solvable properly,
    but for the sake of testing, I will consider it's OK.
    """
    def test_search_bfs(self):
        state = list(range(9))
        random.shuffle(state)
        is_solvable = checks.check_solvable(state)

        print("[ bfs ] testing BFS with state: ", state)

        if is_solvable:
            self.assertTrue(algorithms.search(state, 'bfs'))
        else:
            with self.assertRaises(UnsolvableConfigurationError):
                algorithms.search(state, 'bfs')

    def test_search_iddfs(self):
        state = list(range(9))
        random.shuffle(state)
        is_solvable = checks.check_solvable(state)

        print("[iddfs] testing IDDFS with state: ", state)

        if is_solvable:
            limit = 100000
            tx = 10000
            self.assertTrue(algorithms.iddfs(state, limit, tx))
            # Here we can see that the test will fail
            # if the limit = 100000 has been reached with no success,
            # whether or not there are solutions beyond the defined limit.
            # TODO: add random limit and tx
        else:
            with self.assertRaises(UnsolvableConfigurationError):
                algorithms.search(state, 'bfs')

    def test_search_dfs(self):
        state = list(range(9))
        random.shuffle(state)
        is_solvable = checks.check_solvable(state)

        print("[ dfs ] testing DFS with state: ", state)

        if is_solvable:
            self.assertTrue(algorithms.search(state))
        else:
            with self.assertRaises(UnsolvableConfigurationError):
                algorithms.search(state, 'dfs')


if __name__ == '__main__':
    unittest.main()
