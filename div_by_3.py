'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function div_3 returns True if its single integer parameter is
    divisible by 3 and False otherwise.

EXAMPLE
    div_3(6) is True because 6/3 does not leave any remainder. 
    However, div_3(5) is False because 5/3 leaves 2 as a remainder.
'''

def div_3(input_int):
    ''' Checks whether an integer is divible by 3 '''
    remainder = input_int % 3
    
    if remainder == 0:
        print('Yes, it has a remainder of {}'.format(remainder))
        return True
    else:
        print('No, it has a remainder of {}'.format(remainder))
        return False


# run test 1
print('Test 1'.center(40,'-'))
input_int = 6
print('Check: Is {} divisible by 3?'.format(input_int))
divisible_bool = div_3(input_int)
if divisible_bool == True:
    print('Test passed\n')
else:
    print('Test failed\n')
    
# run test 2
print('Test 2'.center(40,'-'))
input_int = 5
print('Check: Is {} divisible by 3?'.format(input_int))
divisible_bool = div_3(input_int)
if divisible_bool == False:
    print('Test passed\n')
else:
    print('Test failed\n')
