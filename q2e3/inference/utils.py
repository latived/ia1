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
        pass
        rules_base = {}
        facts_base = {}
        with open(file_name) as rules:
            for rule in rules:
                props = re.split('[IF|AND|THEN]', rule)
                if len(props) == 1:
                    if len(props[0]) > 0:
                        facts_base.append(props[0].split('\n')[0])
                    continue
                while '' in props:
                    props.remove('')
                csq = props[-1]
                csq = csq[1:len(csq)-1]
                antecedents = []
                for ant in props[:len(props)-1]:
                    antecedents.append(ant[1:len(ant)-1])
                if csq not in rules_base:
                    rules_base[csq] = []
                    rules_base[csq].extend(antecedents)
                else:
                    rules_base[csq].extend(antecedents)

        return [rules_base, facts_base]

    @staticmethod
    def get_new_facts(cls):
        pass

    @staticmethod
    def verify_goal(goal_to_check):
        pass

    @staticmethod
    def validate_rule(ant, csq):
        # An invalid rule is a rule that
        #   - has repeated premises
        #   - consequent mixed in antecedents
        #   - has already been added
        #   - obviously can't be blank
        if ant == '' or csq == '':
            raise InvalidRuleError("You can't have a blank rule!")

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
    def add_fact(fact):
        if fact == '':
            return False
        elif ' ' in fact:
            print(">! Premises variables can't contain spaces. Type again, please.")
        elif RulesUtils._check_for_punctuation(fact):
            print(">! Premises variables can contain only '_' as punctuation. Type again, please.")
        else:
            Rule.facts.append(fact)

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

    @staticmethod
    def show_rules():
        if len(Rule.rules):
            print(">>> RULES <<<")
            for rule in Rule.rules:
                print('\t' + str(rule))
        print('\n')

