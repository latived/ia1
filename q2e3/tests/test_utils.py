import random
import string
import unittest

from ia1.q2e3.inference.exceptions import InputError, InvalidRuleError, InvalidDuplicateRuleError
from ia1.q2e3.inference.rules import Rule
from ia1.q2e3.inference.utils import InputUtils, RulesUtils


class UtilsTest(unittest.TestCase):

    @staticmethod
    def _random_string(min_char=8, max_char=12):
        allchar = string.ascii_letters + string.punctuation + string.digits
        random_string = "".join(
            random.choice(allchar) for _ in range(
                random.randint(min_char, max_char)))
        return random_string

    def test_check_input_not_ok(self):
        # Just test for 'yes' and 'no'
        with self.assertRaises(InputError):
            InputUtils.check_input_ok(UtilsTest._random_string())

    def test_check_input_ok(self):
        self.assertTrue(InputUtils.check_input_ok('yes'))
        self.assertTrue(InputUtils.check_input_ok('no'))
        self.assertTrue(InputUtils.check_input_ok('stop', True))

    def test_check_input_stop_but_false(self):
        with self.assertRaises(InputError, msg="Expected 'yes' or 'no' in input."):
            InputUtils.check_input_ok('stop')

    def test_check_input_no_stop_but_true(self):
        with self.assertRaises(InputError, msg="Expected 'yes' or 'no' in input."):
            InputUtils.check_input_ok(UtilsTest._random_string())

    def test_check_path_file_not_ok(self):
        self.assertFalse(InputUtils.check_path_file_ok(UtilsTest._random_string()))

    def test_check_path_file_ok(self):
        fn = 'file_database_rules'
        open(file=fn, mode='w', encoding='utf8', newline='\n').close()
        self.assertTrue(InputUtils.check_path_file_ok(fn))

    def test_check_strategy_not_ok(self):
        with self.assertRaises(InputError, msg='Strategy not found.'):
            InputUtils.check_strategy_ok(random.randint(3, 1000000))

    def test_check_strategy_ok(self):
        self.assertTrue(InputUtils.check_strategy_ok(random.choice([1, 3])))


class RulesUtilsTest(unittest.TestCase):

    def test_validate_rule_csq_in_ant(self):
        antecedents = ['p1', 'p2', 'p3']
        consequent = 'p3'
        msg = "You can't have a consequent, '{}', in the antecedents.".format(consequent)
        with self.assertRaises(InvalidRuleError, msg=msg):
            RulesUtils.validate_rule(antecedents, consequent)

    def test_validate_rule_ant_repeating(self):
        antecedents = ['p1', 'p1', 'p2']
        consequent = 'p3'
        msg_error = "You can't have a premise more than once in antecedents."
        with self.assertRaises(InvalidRuleError, msg=msg_error):
            RulesUtils.validate_rule(antecedents, consequent)

    def test_validate_rule_for_duplicates(self):
        antecedent = ['p1', 'p2', 'p3']
        csq = 'p4'
        RulesUtils.create_rule(antecedent, csq)
        msg_error = "This rule already exists!"
        with self.assertRaises(InvalidDuplicateRuleError, msg=msg_error):
            RulesUtils.validate_rule(antecedent, csq)

    def test_add_fact_false(self):
        fact = ''
        self.assertFalse(RulesUtils.add_fact(fact))

    def test_add_fact_true(self):
        fact_w_sp = UtilsTest._random_string(2, 4) + ' ' + UtilsTest._random_string(2, 4)
        fact_wo_sp = UtilsTest._random_string(8, 12)
        self.assertTrue(RulesUtils.add_fact(fact_w_sp))
        self.assertTrue(RulesUtils.add_fact(fact_wo_sp))

    def test_check_for_facts(self):
        self.assertTrue(False)

    # Try to use mock patchs, mocks for input from user...
    def test_get_rules_from_file(self):
        self.assertTrue(False)

    def test_get_rules_from_user(self):
        self.assertTrue(False)

    def test_save_rules_to_file(self):
        self.assertTrue(False)

    def test_create_rule(self):
        self.assertTrue(False)

    def test_get_new_facts(self):
        self.assertTrue(False)

    def test_verify_goal(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
