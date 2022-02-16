'''
PURPOSE
    The function named only_ints takes two parameters. 
    The function returns True if both parameters are integers, and
    False otherwise.
    
EXAMPLE
    Calling only_ints(1, 2) should return True, while calling
    only_ints("a", 1) should return False.
'''

def only_ints(first_var, second_var):
    if type(first_var) is int and type(second_var) is int:
        return True
    else:
        return False

first_var = 1
second_var = 2
both_int_bool = only_ints(first_var, second_var)
print('Are both variables of type int? {}'.format(both_int_bool))
