
class Rule:

    """
    Each rule is a tuple like (antecedents, operator, consequent).

    A premise is a variable like 'will_rain' or 'temperature_less_than_20'.

    Antecedents is one or more premises in a conjunction, like p AND ... AND q.
    Operator here is always the 'equal'.
    Consequent is any other premise.

    Class variables:
        rules -- a list of Rules
        facts -- a list of premises known to be True

    Instance variables:
        antecedent -- a list of premises
        consequent -- any other premise
    """

    rules = []
    facts = []

    def __init__(self, antecedent, consequent):
        self.id = len(Rule.rules) + 1
        self.antecedent = set(antecedent)
        self.consequent = consequent

    def __str__(self):
        out_rule = """
        {}: IF {}
           THEN {}""".format(self.id,
                             ' AND '.join(self.antecedent),
                             self.consequent)
        return out_rule

