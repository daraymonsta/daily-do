'''
WRITTEN BY Ramon Rossi

PURPOSE
    The Greatest Common Divisor (GCD) of two integers is the largest
    natural number that divides these numbers without a remainder.
    
    The function greatest_common_divisor accepts numbers as two 
    arguments. The GCD is returned.
    
EXAMPLE
    For the numbers 32 and 48, the greatest common divisor is 16.
    greatest_common_divisor(32, 48) will return 16.
'''

def greatest_common_divisor(num1, num2):
    greatest_divisor = 0 
    # get the smallest number of num1 and num2
    if num1 < num2:
        smaller_num = num1
    else:
        smaller_num = num2
    
    for x in range(1, smaller_num+1):
        # if both numbers divide evenly by x
        if num1 % x == 0 and num2 % x == 0:
            if x > greatest_divisor:
                greatest_divisor = x 
    
    return greatest_divisor

# run test 1 
print('Test 1'.center(40, '-'))

num1 = 32
num2 = 48
result = greatest_common_divisor(num1, num2)
print('Greatest Common Divisor of {} and {} is {}'.format(num1, num2, result))

if result == 16:
    print('Test passed')
else:
    print('Test failed')
    

# run test 2 
print('Test 2'.center(40, '-'))
num1 = 48
num2 = 60
result = greatest_common_divisor(num1, num2)
print('Greatest Common Divisor of {} and {} is {}'.format(num1, num2, result))

if result == 12:
    print('Test passed')
else:
    print('Test failed')