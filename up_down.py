'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function named up_down takes a single number as 
    its parameter.  It should return a tuple containing
    two numbers; the first should be one lower than the
    parameter, and the second should be one higher.

EXAMPLE
    calling up_down(5) should return (4, 6).
'''

def up_down(input_int):
    ''' Returns a tuple of numbers, one higher and 
        one lower than the input int '''
    num_above = input_int + 1
    num_below = input_int - 1
    return (num_below, num_above)

# run test 1
print('Test 1'.center(40, '-'))
input_int = 5
# call function
result_tuple = up_down(input_int)
# check result
if result_tuple == (4, 6):
    print('Test passed\n')
else:
    print('Test failed\n')
    
# run test 2
print('Test 2'.center(40, '-'))
input_int = 10
# call function
result_tuple = up_down(input_int)
# check result
if result_tuple == (9, 11):
    print('Test passed\n')
else:
    print('Test failed\n')