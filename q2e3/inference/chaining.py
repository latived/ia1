from ia1.q2e3.inference.rules import Rule


class ChainingStrategy:
    @staticmethod
    def backward(goals):
        if type(goals) == str:
            goals = [goals]

        for goal in goals[:]:
            if goal in Rule.facts:
                goals.remove(goal)

        if len(goals) == 0:
            return True

        actual_goal = goals.pop()

        for rule in Rule.rules:
            if actual_goal == rule.consequent:
                goals.extend(rule.antecedent)
            else:
                return False

        return ChainingStrategy.backward(goals)

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
