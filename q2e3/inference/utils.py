import re

from ia1.q2e3.inference.exceptions import InputError, InvalidRuleError, InvalidDuplicateRuleError
from ia1.q2e3.inference.rules import Rule


class InputUtils:
    @staticmethod
    def check_input_ok(input_to_check, possible_stop=False):
        if input_to_check in ['yes', 'no']:
            return True
        else:
            if possible_stop and input_to_check == 'stop':
                return True

        raise InputError(input_to_check, "Expected 'yes' or 'no' in input.")

    @staticmethod
    def check_path_file_ok(path_file_to_check):
        try:
            open(path_file_to_check).close()  # Is there a better way?
            return True
        except FileNotFoundError:
            print('>! Database file not found.')
            return False

    @staticmethod
    def check_strategy_ok(strategy_to_check):
        if strategy_to_check in [1, 2, 3]:
            return True

        raise InputError(strategy_to_check, "Strategy not found.")


class RulesUtils:

    @staticmethod
    def get_rules_from_user():
        antecedents = []
        print('Type new rule below: \n')
        print('IF')
        while True:
            prm = input('  ')
            # TODO: validate premises
            if prm == '':
                break
            else:
                antecedents.append(prm)
        print('THEN')
        consequent = input('  ')
        # TODO: validate premises

        return antecedents, consequent

    @staticmethod
    def save_rules_to_file():
        print("Type a name for the database file: ")
        name = input('> ')
        # TODO: need to check for existing files?
        with open(name, mode='w', encoding='utf-8', newline='\n') as db:
            for rule in Rule.rules:
                print('IF ' + ' AND '.join(rule.antecedent) + ' THEN ' + rule.consequent, file=db)
            for fact in Rule.facts:
                print(fact, file=db)
        print("Database saved in a file as '{}'.".format(name))

    # FIXME: update this method to accommodate changes
    @staticmethod
    def get_rules_from_file(file_name):
        with open(file_name) as rules:
            for rule in rules:
                # This you do:
                #       IF p1 AND ... AND pn THEN csq
                # in    [
                props = re.split('[IF|AND|THEN]', rule.replace(' ', ''))
                if len(props) == 1:
                    if len(props[0]) > 0:
                        Rule.facts.append(props[0].split('\n')[0])
                    continue
                csq = props.pop()[:-1]  # Pop consequent without '\n'
                antecedent = []
                for item in props:
                    if item != '':
                        antecedent.append(item)

                # TODO: add validate_rule here? or inside create_rule?
                RulesUtils.create_rule(antecedent, csq)

    @staticmethod
    def get_new_facts(cls):
        pass

    @staticmethod
    def validate_rule(ant, csq):
        # An invalid rule is a rule that
        #   - has repeated premises
        #   - consequent mixed in antecedents
        #   - has already been added
        #   - obviously can't be blank
        if '' in ant or csq:
            raise InvalidRuleError("You can't have a blank rule!")

        for var in ant+csq:
            if not RulesUtils.check_variable(var, log=False):  # TODO: test for it
                InvalidRuleError("A variable can not have spaces or punctuations.")

        sz_set_ant = len(set(ant))
        sz_list_ant = len(ant)
        if sz_list_ant != sz_set_ant:
            raise InvalidRuleError("You can't have a premise more than once in antecedents.")

        if csq in ant:
            msg_error = "You can't have a consequent, '{}', in the antecedents.".format(csq)
            raise InvalidRuleError(msg_error)

        # TODO: is it better to wrap this verification of duplicates below?
        ant = set(ant)
        for rule in Rule.rules:
            if (ant, csq) == (rule.antecedent, rule.consequent):
                msg_error = "This rule already exists!"
                raise InvalidDuplicateRuleError(msg_error)

    @staticmethod
    def _check_for_punctuation(fact):
        from string import punctuation
        for c in list(fact.replace('_', '')):
            if c in punctuation:
                return True
        return False

    @staticmethod
    def add_fact(fact):  # TODO: test for changes
        if RulesUtils.check_variable(fact):
            Rule.facts.append(fact)
            return True
        return False

    @staticmethod
    def check_variable(variable, log=True):  # TODO: test for changes
        if ' ' in variable:
            if log:
                print(">! Premises variables can't contain spaces. Type again, please.")
            return False
        elif RulesUtils._check_for_punctuation(variable):
            if log:
                print(">! Premises variables can contain only '_' as punctuation. Type again, please.")
            return False

        return True

    @staticmethod
    def check_for_facts():
        return len(Rule.facts) > 0

    @staticmethod
    def check_for_rules():
        return len(Rule.rules) > 0

    @staticmethod
    def create_rule(ant, csq):
        # TODO: could add the validate_rule here?
        # NO, because we have other statements between validate and create
        rule = Rule(ant, csq)
        Rule.rules.append(rule)

    @staticmethod
    def update_rules(id, ant, csq):
        pass

    @staticmethod
    def get_rule(id):
        return None

    @staticmethod
    def show_rule(ant, csq):
        rule = 'IF ' + ' AND '.join(ant) + ' THEN ' + csq
        return rule

    # TODO: show_facts
    @staticmethod
    def show_rules():
        if len(Rule.rules):
            print(">>> RULES <<<")
            for rule in Rule.rules:
                print('\t' + str(rule))
        print('\n')

