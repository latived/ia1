#!/usr/bin/env python3

import re

# goal-driven search
def backward(goals, rules_base, facts_base):
    if type(goals) == str:
        goals = [goals]

    ite_goals = goals.copy()
    for goal in ite_goals:
        if goal in facts_base:
            goals.remove(goal)

    if len(goals) == 0:
        print("goal proved true!")
        return True

    new_goal = goals[0]
    goals.remove(new_goal)
    
    if new_goal in rules_base:
        antecedents = rules_base[new_goal].copy()
    else:
        print("couldn't prove goal with given rules' and facts' base.")
        return False
    
    return backward(antecedents, rules_base, facts_base) 

# data-driven search
def forward(rules_base, facts_base, pos=0):
    if pos == len(rules_base):
        return True

    csq = list(rules_base.keys())[pos]
    
    antecedents = rules_base[csq].copy()

    if csq not in facts_base:
        for ant in rules_base[csq]:
            if ant in facts_base:
                antecedents.remove(ant)
        
        if len(antecedents) == 0:
            facts_base.append(csq)
            pos = -1

    return forward(rules_base, facts_base, pos+1)

def get_rules(file_name):
    rules_base = {}
    facts_base = {}
    with open(file_name) as rules:
        for rule in rules:
            props = re.split('[IF|AND|THEN]', rule)
            if len(props) == 1:
                if len(props[0]) > 0: facts_base.append(props[0].split('\n')[0])
                continue
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
                rules_base[csq].extend(antecedents)

    return [rules_base, facts_base]

def check_value(value):
    if value == "1":
        return True
    elif value == "0":
        return False
    else:
        raise ValueError("Valor não permitido!")

def show_rules(rules_base):
    print("Rules' base: ")
    for rule in rules_base:
        print("\tIF " + " AND ".join(rules_base[rule]) + " THEN " + rule)

def show_facts(facts_base):
    print("Facts' base: ")
    for fact in facts_base:
        print("\t" + fact)

def main():
    rules_base, facts_base = get_rules('rules_base')
    show_rules(rules_base)
    show_facts(facts_base)
    print('\n')
    goal = input("Goal for backward chaining (try 'green'): ")
    #value = input("Value for " + goal + " (1 for true, 0 for false) = ")
    #check_value(value)
    print('\n')
    
    print("Testing backward chaining for... '", goal, "'")
    backward(goal, rules_base, facts_base)
    print('\n')
    
    print("Testing what forward chaining can give us...")
    rules_base, facts_base = get_rules('rules_base')
    forward(rules_base, facts_base)
    print("Facts base after forward chaining: \n", facts_base)

if __name__ == "__main__":
    main()
