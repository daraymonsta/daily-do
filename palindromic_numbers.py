'''
WRITTEN BY Ramon Rossi

PURPOSE
    Consider palindromic numbers. A palindromic or symmetric number is
    a number that does not change when you write its digits in reverse
    order.
    
EXAMPLE
    calculate(3) will calculate the number of 3 digit palindromic 
    numbers. The result should be 90.
    
    Some of the numbers included will be... 363, 545, 717
'''

def calculate(no_digits):
    # initialise variables
    palindromic_count = 0
    if no_digits == 1:
        min_int = 0 
        max_int = 9
    else:
        min_int = int(str('9'*(no_digits-1)))+1
        max_int = int(str('9'*no_digits))
    
    # loop through all numbers checking if palindromic
    for x in range(min_int, max_int+1):
        original_str = str(x)
        revsersed_str = original_str[::-1]
        
        # check if the number is the same in reverse
        if original_str == revsersed_str:
            print(original_str)
            # add 1 to palindromic count
            palindromic_count += 1
    
    return palindromic_count

# run test 1 
print('Test 1'.center(40,'-'))
no_digits = 3
result = calculate(no_digits)
print('Number of palindromic {}-digit numbers: {}'.format(no_digits, result))
if result == 90:
    print('Test passed')
else:
    print('Test failed')