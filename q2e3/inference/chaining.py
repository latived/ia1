from ia1.q2e3.inference.rules import Rule


# TODO: conflict resolution
class ChainingStrategy:
    """
    Backward and forward methods as in:
        http://www-personal.umd.umich.edu/~leortiz/teaching/6.034f/Fall05/rules/fwd_bck.pdf
    """

    explanation_tree = {}

    @staticmethod
    def show_explanation_tree(root, levels=49, spaces=0):
        if levels == 49:
            print('\n')
            print(root + ': ')
        if root in ChainingStrategy.explanation_tree.keys():
            # print("{}{}: {}".format((7-levels)*'\t', root, ChainingStrategy.explanation_tree[root]))
            for leaf in ChainingStrategy.explanation_tree[root]:
                print('{}{} '.format(spaces*'| '+'\\_'+(49-levels)*'_', leaf))
                ChainingStrategy.show_explanation_tree(leaf, levels-7, spaces+1)

    @staticmethod
    def backward(goal):
        #print("trying: {}".format(goal))
        if goal in Rule.facts:
            return True

        matches = [rule for rule in Rule.rules if goal == rule.consequent]

        if not len(matches):
            return False
        else:
            for rule in matches:
                results = [ChainingStrategy.backward(premise) for premise in rule.antecedent]
                #print("result(s) for {} child(ren) {}: {}".format(rule.consequent, rule.antecedent, results))
                if all(results):
                    ChainingStrategy.explanation_tree[rule.consequent] = {premise for premise in rule.antecedent}
                    return True
            return False

    @staticmethod
    def forward():
        new_facts = Rule.facts[:]
        recent_added = []

        def in_facts(premise):
            return premise in new_facts

        def add(csq):
            new_facts.append(csq)
            recent_added.append(csq)

        has_changed = True
        while has_changed:
            has_changed = False
            for rule in Rule.rules:
                matches = [in_facts(premise) for premise in rule.antecedent]
                if all(matches) and not in_facts(rule.consequent):
                    add(rule.consequent)
                    has_changed = True

        return recent_added
