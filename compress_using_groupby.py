'''
WRITTEN BY Ramon Rossi

PURPOSE
    The compress function runs a compression algorithm on the input number 
    passed as a input parameter.  The algorithm goes from left to right
    through each digit and returns a list of two-element tuples.  Each tuple
    consists of a digit and the number of repetitions of a given digit until
    the next, different digit in the number is encountered.
    
    Note: This uses the groupby function in itertools to reduce the code to
    compress.

EXAMPLE
    compress(111) returns [('1', 3]
    
    compress(1000000) returns [('1', 1), ('0', 6)]
    
    compress(10005000) returns [('1', 1), ('0', 3), ('5', 1), ('0', 3)]
'''

from itertools import groupby

def compress(number_to_compress):
    print('Number to compress is {}'.format(number_to_compress))
    # initialise list
    compressed_list = []
    for key, group in groupby(str(number_to_compress)):
        # save in list
        compressed_list.append((key, len(list(group))))

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