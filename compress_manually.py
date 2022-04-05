'''
WRITTEN BY Ramon Rossi

PURPOSE
    The compress function runs a compression algorithm on the input number 
    passed as a input parameter.  The algorithm goes from left to right
    through each digit and returns a list of two-element tuples.  Each tuple
    consists of a digit and the number of repetitions of a given digit until
    the next, different digit in the number is encountered.
    
    Note: Although there are Python functions that could be imported to help,
    the challenge was to do it manually.

EXAMPLE
    compress(111) returns [('1', 3]
    
    compress(1000000) returns [('1', 1), ('0', 6)]
    
    compress(10005000) returns [('1', 1), ('0', 3), ('5', 1), ('0', 3)]
'''

def compress(number_to_compress):
    print('Number to compress is {}'.format(number_to_compress))
    # it will be easer to compress if it's a string
    temp_str = str(number_to_compress)
    counter = 0
    compressed_list = []
    # print('length of str = {}'.format(len(temp_str)))
    
    # loop through each character of the number
    for x in range(len(temp_str)):
        if x == 0:  # first character
            # store it as the previous character
            prev_character = temp_str[0]
            counter = 1
            if x == len(temp_str)-1: # string has only 1 character total
                compressed_list.append((prev_character, counter))
        else:
            if temp_str[x] == prev_character:
                counter += 1
                if x == (len(temp_str)-1): # up to last character
                    compressed_list.append((prev_character, counter))
            else:
                # store how many of the previous character before
                # resetting the counter
                compressed_list.append((prev_character, counter))
                counter = 1
                
            prev_character = temp_str[x]
        # print(x)
        # print('counter = {}'.format(counter))
    
    print('After compression... {}'.format(compressed_list))
    
    return compressed_list

# run test 1 
print('Test 1'.center(40,'-'))
number_to_compress = 111
result_list = compress(number_to_compress)
if result_list == [('1', 3)]:
    print('Test passed')
else:
    print('Test failed')
    
# run test 2
print('Test 2'.center(40,'-'))
number_to_compress = 1000000
result_list = compress(number_to_compress)
if result_list == [('1', 1), ('0', 6)]:
    print('Test passed')
else:
    print('Test failed')
    
# run test 3
print('Test 3'.center(40,'-'))
number_to_compress = 10005000
result_list = compress(number_to_compress)
if result_list == [('1', 1), ('0', 3), ('5', 1), ('0', 3)]:
    print('Test passed')
else:
    print('Test failed')