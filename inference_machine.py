#!/usr/bin/env python3

import re

# goal-driven search
def backward(goals, rules_base, facts_base):
    print("Goals to be proved: ", goals)

    if type(goals) == str:
        goals = [goals]

    ite_goals = goals.copy()
    for goal in ite_goals:
        if goal in facts_base:
            print(goal, "in facts' base!")
            goals.remove(goal)

    if len(goals) == 0:
        print("Goals proved!")
        return True

    print("Remaining goals: ", goals)
    new_goal = goals[0]
    goals.remove(new_goal)
    
    if new_goal in rules_base:
        antecedents = rules_base[new_goal].copy()
    else:
        print("'", new_goal, "' not in rules base! Can't prove...")
        return False
    
    return backward(antecedents, rules_base, facts_base) 

# data-driven search
def forward(goal, rules_base, facts_base, pos=0):
    print("Goal to be proved '", goal, "'")
    if goal in facts_base:
        print("'", goal, "' found in facts' base! Proved :)")
        return True

    if pos == len(rules_base):
        print("Can't prove that '", goal, "' is true with the given rules' base.")
        return False

    csq = list(rules_base.keys())[pos]
    print("Trying to prove '", csq, "'")
    
    antecedents = rules_base[csq].copy()
    print("\tNeed to check: ", antecedents)

    if csq not in facts_base:
        for ant in rules_base[csq]:
            if ant in facts_base:
                print("\t'",ant, "' in facts' base!")
                antecedents.remove(ant)
        
        if len(antecedents) == 0:
            print("\tFacts' base updated with '",csq,"'! Starting again from first rule...")
            facts_base.append(csq)
            pos = 0
        else:
            print("\tCouldn't prove the remaining antecedents yet: ", antecedents)
    else:
        print("'",csq,"' already in facts' base!")

    return forward(goal, rules_base, facts_base, pos+1)

def main():
    rules_base = {}
    with open("rules_base") as rules:
        for rule in rules:
            props = re.split('[IF|AND|THEN]', rule)
            if len(props) == 1:
                break
            while '' in props: props.remove('')
            csq = props[-1]
            csq = csq[1:len(csq)-1]
            antecedents = []
            for ant in props[:len(props)-1]:
                antecedents.append(ant[1:len(ant)-1])
            if csq not in rules_base:
                rules_base[csq] = []
                rules_base[csq].extend(antecedents)
            else:
                rules_base[csq.extend(antecedents)

    facts_base = ["croaks", "eats flies"]
    goal = "is green"
    
    print("Testing backward chaining for... 'X ", goal, "'")
    backward(goal, rules_base, facts_base)
    print("... # # # ...")
    print("Testing forward chaining for... 'X ", goal, "'")
    forward(goal, rules_base, facts_base)

if __name__ == "__main__":
    main()
