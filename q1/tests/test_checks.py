import random
import unittest
from ..code import checks


class ChecksTest(unittest.TestCase):

    # TODO: break this test in two (for oks, for fails)
    def test_check_is_state_solvable(self):
        state_ok = [1, 2, 3,
                    4, 5, 6,
                    7, 8, 0]  # no permutations at all

        state_fail = [1, 2, 3,
                      4, 5, 6,
                      8, 7, 0]  # odd number of permutations

        # TODO: how can I add more states without writing them at first?
        # Maybe writing a even/odd state generator.

        self.assertTrue(checks.check_solvable(state_ok))
        self.assertFalse(checks.check_solvable(state_fail))

    def test_check_state_goal_ok(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.assertTrue(checks.check_state_is_goal(goal))

    def test_check_state_goal_not_ok(self):
        # A complex test to a simple method.

        # Now we test for failures.
        # random.shuffle uses Mersenne Twister random number generator (RNG)
        # This generator has a maximum size of 2080 numbers for its sequence.
        # Therefore, we only test for this total, aware that some permutations
        # will not be tested.
        # TODO: find another RNG.
        for _ in range(2080):
            not_goal = list(range(9))
            # By contract, the actual sorted list (0 to 8)
            # will never be returned.
            random.shuffle(not_goal)
            self.assertFalse(checks.check_state_is_goal(not_goal))

    def test_check_state_not_valid_size(self):
        for sz in range(9):
            state = list(range(sz))
            # size error
            self.assertFalse(checks.check_is_state_valid(state))

    def test_check_state_not_valid_config(self):
        # get list ok
        state = list(range(9))
        # choose one random idx from 0 to 8
        idx = random.randint(0, 8)
        # choose number from an outside interval
        outside_number = random.randint(9, 9999)  # high limit defined arbitrarily.
        # swap state[idx] for outside number
        state[idx] = outside_number
        # test for false
        self.assertFalse(checks.check_is_state_valid(state))

    def test_check_state_is_valid(self):
        for _ in range(2080):
            state = list(range(9))
            random.shuffle(state)
            self.assertTrue(checks.check_is_state_valid(state))

    def test_check_input_for_value_error(self):
        state = 'não vai dar erro.'
        self.assertFalse(checks.check_input_ok(state))

        state = '1 a 2 3 4 5 6 7 0'
        self.assertFalse(checks.check_input_ok(state))

        # TODO: is there any way to generalize this?

    def test_check_input_for_already_solved_state(self):
        state_input = '1 2 3 4 5 6 7 8 0'
        # input solved
        self.assertFalse(checks.check_input_ok(state_input))

    def test_check_input_ok(self):
        for _ in range(2080):
            state_ok = list(range(9))
            random.shuffle(state_ok)
            # [n1, n2, ..., n9] to 'n1 n2 ... n9'
            state_ok = str(state_ok)[1:-1].replace(', ', ' ')
            self.assertTrue(checks.check_input_ok(state_ok))


if __name__ == '__main__':
    unittest.main()
