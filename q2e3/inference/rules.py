
class Rule:

    """
    Each rule is a tuple like (antecedents, operator, consequent).

    A premise is a variable like 'will_rain' or 'temperature_less_than_20'.

    Antecedents is one or more premises in a conjunction, like p AND ... AND q.
    Operator here is always the 'equal'.
    Consequent is any other premise.

    Class variables:
        rules -- a dictionary of Rules
        facts -- a list of premises known to be True

    Instance variables:
        antecedent -- a list of premises
        consequent -- any other premise
    """

    rules = {}
    facts = []

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

