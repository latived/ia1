from ia1.q2e3.inference.chaining import ChainingStrategy
from ia1.q2e3.inference.utils import RulesUtils
from ia1.q2e3.inference.utils import check_input_ok, check_path_file_ok, check_strategy_ok


def main():
    print("Type 'yes' below if you want to tell your own rules (or 'no' for file as input).")
    where_to_get = input('> ')

    # TODO: implement method check_input_ok, and don't forget exception.
    check_input_ok(where_to_get)

    if where_to_get == 'yes':
        RulesUtils.get_rules_from_user()
        print('Rules database now complete.')
    else:
        print('Type the file name below, please. Verify that it is in the same folder as this script.')
        path_file = input('> ')
        # TODO: implement method check_path_file_ok, and don't forget exception.
        check_path_file_ok(path_file)
        RulesUtils.get_rules_from_file(path_file)
        print('Rules and facts loaded!')

    print('\n')
    print("""
    Type now which strategy do you want (type 1 or 2): 
        1. Forward chaining
        2. Backward chaining
        3. Other (not implemented)
    """)

    type_strategy = int(input('> '))
    # TODO: implement method check_strategy_ok, and don't forget exception.
    check_strategy_ok(type_strategy)

    # Rules and facts database will now be class attributes of RulesUtils

    if type_strategy == 1:
        print('Running now forward chaining...')
        ChainingStrategy.forward()
        print('Done.')
        print("Type 'yes' if you want to see the new facts discovered ('no' otherwise).")
        see_facts = input('> ')
        # TODO: implement method check_input_ok, and don't forget exception.
        check_input_ok(see_facts)
        RulesUtils.show_new_facts()
    else:
        print("""
        Type now what you want to prove (with the given database).
        
        Ex.: 'will_rain' or 'temperature_less_than_20'
        
        Anything like that, named as variable. If the question doesn't exists in
        the database, an exception will be raised.
        """)
        goal = input('>')
        # TODO: implement method verify_goal, and don't forget exception.
        RulesUtils.verify_goal(goal)
        print('Running now backward chaining on "{}"...'.format(goal))
        ChainingStrategy.backward(goal)
        print('Done.')


if __name__ == "__main__":
    main()
