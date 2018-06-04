from ia1.q2e3.inference.rules import Rule


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
