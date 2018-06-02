import re

from .rules import Rule


class ChainingStrategy:
    @classmethod
    def backward(cls, goals):
        pass
        if type(goals) == str:
            goals = [goals]

        ite_goals = goals.copy()
        for goal in ite_goals:
            if goal in Rule.facts:
                goals.remove(goal)

        if len(goals) == 0:
            print("goal proved true!")
            return True

        new_goal = goals[0]
        goals.remove(new_goal)

        if new_goal in Rule.rules:
            antecedents = Rule.rules[new_goal].copy()
        else:
            print("couldn't prove goal with given rules' and facts' base.")
            return False

        return cls.backward(antecedents)

    @classmethod
    def forward(cls, pos=0):
        pass
        if pos == len(Rule.rules):
            return True

        csq = list(Rule.rules.keys())[pos]

        antecedents = Rule.rules[csq].copy()

        if csq not in Rule.facts:
            for ant in Rule.rules[csq]:
                if ant in Rule.facts:
                    antecedents.remove(ant)

            if len(antecedents) == 0:
                Rule.facts.append(csq)
                pos = -1

        return cls.forward(pos+1)


class RulesUtils:

    @classmethod
    def get_rules_from_user(cls):
        pass

    @classmethod
    def get_rules_from_file(cls, file_name):
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

    @classmethod
    def show_rules(cls, rules_base):
        print("Rules' base: ")
        for rule in rules_base:
            print("\tIF " + " AND ".join(rules_base[rule]) + " THEN " + rule)

    @classmethod
    def show_facts(cls, facts_base):
        print("Facts' base: ")
        for fact in facts_base:
            print("\t" + fact)

    @classmethod
    def show_new_facts(cls):
        pass

