'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function is_palindrome() accepts the parameter number of digits.
    It then checks all numbers with that number of digits to find numbers
    that are palindromic both as decimal and binary, and returns these as
    a list.

EXAMPLE
    is_palindrome(3) will return [313, 585, 717].
    
NOTES
    Rather than manually converting to decimal to binary (like I did in 
    palindromic_also_binary.py, this code uses the build-in python function
    to do it.
'''

def is_palindrome(num_digits):
    # initialise variable
    palindrome_list = []
    
    # get min test num
    if num_digits == 1:
        min_test_num = '0'
    else:
        min_test_num = '1'*(num_digits-1) + '0'
    
    # get max test num
    max_test_num = '9'*num_digits
    
    # loop through numbers checking for palindromes
    for test_num in range(int(min_test_num), int(max_test_num)):
        # convert to binary
        bin_test_num = bin(test_num)[2:]  # don't want first 2 characters '0b'
        # print('binary number = {}'.format(bin_test_num))
        
        # check if both decimal + binary is palindrome
        if (str(test_num) == str(test_num)[::-1]) and (bin_test_num == bin_test_num[::-1]):
            # save it to list
            palindrome_list.append(test_num)
    
    return palindrome_list
    
# run test 1 
print('Test 1'.center(40,'-'))
num_digits = 3  # 3 means 3-digit numbers
result_list = is_palindrome(num_digits)
print('{} digit numbers which are palindromic as a decimal and binary are...'.format(num_digits))
print(result_list)

if result_list == [313, 585, 717]:
    print('Test passed')
else:
    print('Test failed')