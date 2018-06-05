import unittest

from ia1.q2e3.inference.chaining import ChainingStrategy
from ia1.q2e3.inference.rules import Rule
from ia1.q2e3.inference.utils import RulesUtils


class ChainingStrategyTest(unittest.TestCase):

    def test_01_backward(self):
        RulesUtils.get_rules_from_file('../rules_base')
        goal = 'green'
        goal_false = 'canary'
        self.assertTrue(ChainingStrategy.backward(goal))
        self.assertFalse(ChainingStrategy.backward(goal_false))

    def test_02_backward_easy(self):
        RulesUtils.get_rules_from_file('../rules_base_02')
        goal = 'd'
        goal_false = 'e'    # Not in rules_base_02
        self.assertTrue(ChainingStrategy.backward(goal))
        self.assertFalse(ChainingStrategy.backward(goal_false))

    def test_03_backward_less_easy(self):
        RulesUtils.get_rules_from_file('../rules_base_03')
        goal = 'x'
        goal_false = 'y'    # In rules_base_03 as csq, but need f, which can be proved True.
        self.assertTrue(ChainingStrategy.backward(goal))
        self.assertFalse(ChainingStrategy.backward(goal_false))

    def test_04_backward_almost_not_easy(self):
        RulesUtils.get_rules_from_file('../rules_base_04')
        goal = 'goal'
        goal_false = 'm'    # Need p and q, which can't be proved.
        self.assertTrue(ChainingStrategy.backward(goal))
        self.assertFalse(ChainingStrategy.backward(goal_false))

    def test_05_backward_medium_maybe(self):
        RulesUtils.get_rules_from_file('../rules_base_05')
        goal = 'goal'
        goal_false = 'nao_tem'  # In some rule's antecedent only
        self.assertTrue(ChainingStrategy.backward(goal))
        self.assertFalse(ChainingStrategy.backward(goal_false))

    def test_06_forward(self):
        RulesUtils.get_rules_from_file('../rules_base')
        new_facts = ['frog', 'green']
        self.assertEqual(ChainingStrategy.forward(), new_facts)  # TODO: use RuleUtils.get_new_facts()

    def test_07_forward(self):
        RulesUtils.get_rules_from_file('../rules_base_02')
        new_facts = ['c', 'd']
        self.assertEqual(ChainingStrategy.forward(), new_facts)  # TODO: use RuleUtils.get_new_facts()

    def test_08_forward_left_one(self):
        RulesUtils.get_rules_from_file('../rules_base_03')
        new_facts = ['z', 'w', 'x']
        self.assertEqual(ChainingStrategy.forward(), new_facts)  # ...

    def test_09_forward_duplicate_csq(self):
        RulesUtils.get_rules_from_file('../rules_base_05')
        new_facts = ['v', 'u', 'y', 'x', 'z', 'w', 'goal']
        self.assertEqual(ChainingStrategy.forward(), new_facts)

    def test_10_forward_duplicate_csq_but_satisfiable(self):
        RulesUtils.get_rules_from_file('../rules_base_06')
        # Same as before, but notice in rules_base_06 a rule with goal as csq again, and satisfiable.
        new_facts = ['v', 'u', 'y', 'x', 'z', 'w', 'goal']  # Therefore, we test for no duplicate of goal in new_facts.
        self.assertEqual(ChainingStrategy.forward(), new_facts)

    def tearDown(self):
        RulesUtils.clear_running_database()
