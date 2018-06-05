import string

from ia1.q2e3.inference.chaining import ChainingStrategy
from ia1.q2e3.inference.utils import RulesUtils, InputUtils


def main():
    print("Type 'yes' below if you want to tell your own rules (or 'no' for file as input).")
    where_to_get = input('> ')

    InputUtils.check_input_ok(where_to_get)

    if where_to_get == 'yes':
        print("""
        Type the rules as in the example below (one at a time):
            IF premise_1
                premise_2
                ... 
                premise_n
                
            THEN 
                consequent
            
            Example:
            
            IF will_not_rain
                have_cash 
            THEN 
                go_out_tomorrow
            
        """)
        while True:
            RulesUtils.show_rules()
            antecedents, consequent = RulesUtils.get_rules_from_user()
            RulesUtils.validate_rule(antecedents, consequent)
            print('\nYour rule: ', RulesUtils.show_rule(antecedents, consequent))
            print('Confirm (yes/no)? Also, type "stop" to confirm and terminate here.')
            confirm = input('> ')
            InputUtils.check_input_ok(confirm, possible_stop=True)
            if confirm == 'stop':
                RulesUtils.create_rule(antecedents, consequent)
                break
            elif confirm == 'yes':
                RulesUtils.create_rule(antecedents, consequent)
            else:
                if not RulesUtils.check_for_rules():  # TODO: test check_for_rules
                    print(">! You must add at least one rule.")
                else:
                    print('Do you want to continue? (yes/no)')
                    confirm = input('> ')
                    InputUtils.check_input_ok(confirm)
                    if confirm == 'no':
                        break

        print('Rules database now complete. However, you must add your facts to the database.')
        print("""
        Below, type the variables that you know are TRUE (blank line for stop).
        Example (notice the blank line): 
            > will_rain
            > go_out_tomorrow
            >         
        
        """)
        while True:
            fact = input('> ')
            if not fact:
                if not RulesUtils.check_for_facts():  # TODO: check_for_facts NOT TESTED
                    print(">! No facts have been added till now. "
                          "You really wishes to continue (yes/no)? "
                          "You will not be able to prove anything.")
                    confirm = input('> ')
                    InputUtils.check_input_ok(confirm)
                    if confirm == 'yes':
                        break
                break
            elif RulesUtils.add_fact(fact):
                continue

        print('Facts added to the database.')
        RulesUtils.save_rules_to_file()
    else:
        # TODO: this else is not tested
        print('Type the file name below, please. Verify that it is in the same folder as this script.')
        while True:
            path_file = input('> ')
            if InputUtils.check_path_file_ok(path_file):
                RulesUtils.get_rules_from_file(path_file)
                print('Rules and facts loaded!')
                break

        RulesUtils.show_rules()

    print('\n')
    print("""
    Type now which strategy do you want (type 1 or 2): 
        1. Forward chaining
        2. Backward chaining
        3. Other (not implemented)
    """)

    type_strategy = int(input('> '))
    InputUtils.check_strategy_ok(type_strategy)

    # Rules and facts database will now be class attributes of RulesUtils

    if type_strategy == 1:
        print('Running now forward chaining...')
        new_facts = ChainingStrategy.forward()
        print('Done.')
        print('Showing new facts...')
        RulesUtils.show_new_facts(new_facts)
        print("Type 'yes' if you want to save the new facts discovered ('no' otherwise).")
        save_facts = input('> ')
        InputUtils.check_input_ok(save_facts)
        if save_facts == 'yes':
            RulesUtils.merge_new_facts(new_facts)
            RulesUtils.save_rules_to_file()
        print('Bye!')
    elif type_strategy == 2:
        print("""
        Type now what you want to prove (with the given database).
        
        Ex.: 'will_rain' or 'temperature_less_than_20'
        
        Anything like that, named as variable. 
        """)
        while True:
            goal = input('>')
            if RulesUtils.check_variable(goal):
                break

        print('Running now backward chaining on "{}"...'.format(goal))
        result_msg = 'Based on the existing database, we have {} = {}.'
        if ChainingStrategy.backward(goal):
            print(result_msg.format(goal, True))
        else:
            print(result_msg.format(goal, False))
        print('Done.')
    else:
        print("Not implemented yet.")


if __name__ == "__main__":
    main()
