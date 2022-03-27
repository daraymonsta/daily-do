'''
WRITTEN BY Ramon Rossi

PURPOSE
    A palindromic number is a number that does not change when you write 
    its digits in reverse.
    
    The function calculate() returns the largest palindromic number resulting
    from the product of x-digit numbers.
    
EXAMPLE
    calculate(2) will find the largest palindromic number which is the
    product of 2-digit numbers.  The result should be 9009.
'''

def calculate(num_digits):
    largest_pal_num_so_far = 0
    
    if num_digits == 1:
        min_int = 1
    else:
        min_int = int('1' + '0'*(num_digits-1))
    max_int = int('9'*num_digits)
    
    print('Min = {}, Max = {}'.format(min_int, max_int))
    for x in range(min_int, max_int+1):
        for y in range(min_int, max_int+1):
            temp_int = x*y
            original_string = str(temp_int)
            reversed_string = str(temp_int)[::-1]
            if original_string == reversed_string:
                print('{} is palindromic!'.format(temp_int))
                if temp_int > largest_pal_num_so_far:
                    largest_pal_num_so_far = temp_int
    
    return largest_pal_num_so_far

# run test 1 
print('Test 1'.center(40, '-'))

num_digits = 2
result = calculate(num_digits)
print('Largest palindromic number = {}'.format(result))
if result == 9009:
    print('Test passed')
else:
    print('Test failed')