'''
WRITTEN BY Ramon Rossi

PURPOSE
    A palindromic number is a number that does not change when you write 
    its digits in reverse order e.g. 363, 2882.
    
    The function is_palindrome checks if the number passed to it is
    palindromic both as a decimal and binary number.  If both conditions are 
    met, the function returns True, otherwise False.
    
EXAMPLE
    is_palindrome(99) is a palindromic number as a decimal and its binary
    notation 1100011 is also a palindrome.  Since both conditions are 
    met, the function returns True.
'''

def is_palindrome(temp_int):
    
    # 1. reverse the decimal of the number
    temp_str = str(temp_int)
    reversed_temp_str = temp_str[::-1]
    print('The reverse of number {} is {}'.format(temp_str, reversed_temp_str))
    
    # 2. convert the decimal number to a binary number
    # initilise variables
    power_result_list = []
    x = 0
    
    # get the powers of 2 in a list
    while True:
        if 2**x > temp_int:
            # reached one power too high, go back one power
            x -= 1
            break
        power_result_list.append(2**x)
        x += 1
        
    # reverse the powers of 2 values list
    power_result_list = power_result_list[::-1]
    # print('x is {}'.format(x))
    # print(power_result_list)
    
    # initilise variables for the next bit
    left_int = temp_int
    binary_result_list = []
    i = 0
    
    # use the powers of 2 values to generate the binary number
    while left_int != 0:
        if left_int >= power_result_list[i]:
            left_int = left_int - power_result_list[i]
            # add 1 to binary result
            binary_result_list.append(1)
        else:
            # add 0 to binary result
            binary_result_list.append(0)
        i += 1
    
    # reverse the binary number
    temp_binary_str = ''.join(str(e) for e in binary_result_list)
    reversed_temp_binary_str = temp_binary_str[::-1]
    print('The reverse of binary number {} is {}'.format(temp_binary_str, reversed_temp_binary_str))

    if (temp_str == reversed_temp_str) and (temp_binary_str == reversed_temp_binary_str):
        return True
    else:
        return False
    
# run test 1 
print('Test 1'.center(40,'-'))

temp_int = 99
result = is_palindrome(temp_int)
if result:
    print('Test passed')
else:
    print('Test failed')