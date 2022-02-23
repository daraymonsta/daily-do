'''
WRITTEN BY Ramon Rossi

PURPOSE
    A string is a palindrome when it is the same when
    read backwards.
    
    The function named palindrome that takes a single string 
    as its parameter. It returns True if the string is a 
    palindrome, and False otherwise.
    
EXAMPLE
    The string "bob" is a palindrome. So is "abba". But the string 
    "abcd" is not a palindrome, because "abcd" != "dcba".
'''

def palindrome(input_str):
    print('Original string is "{}"'.format(input_str))
    
    num_chars = len(input_str)
    # create an empty list with the same number of places
    # as the number of letters in the original string
    temp_list = [None] * num_chars
    
    # loop through characters in string in order
    for x in range(len(input_str)):
        # start with last position in list and
        # work backwards, adding a letter at a time
        # as it loops
        temp_list[num_chars-1-x] = input_str[x]
        
    # convert the list of reversed characters
    # back into a string
    reversed_str = ''.join(temp_list)
    print('Reversed string is "{}"'.format(reversed_str))
    if input_str == reversed_str:
        print('Result: It is a palindrome')
        return True
    else:
        print('Result: It is not a palindrome')
        return False

# run test 1
print('Test 1'.center(40,'-'))
input_str = "abbaaa"
whether_palindrome = palindrome(input_str)
if whether_palindrome == False:
    print('Test passed\n')
else:
    print('Test failed\n')
    
# run test 2
print('Test 2'.center(40,'-'))
input_str = "abba"
whether_palindrome = palindrome(input_str)
if whether_palindrome == True:
    print('Test passed\n')
else:
    print('Test failed\n')