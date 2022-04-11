'''
WRITTEN BY Ramon Rossi
 
PURPOSE
    The function compress() accepts as input parameter a number to
    compress.  The functions returns a string of the compressed digits.
    To compress the number, each digit is stored along with the number
    of times that digit repeats.  Each pair such is separated by the
    underscore (_) character.
    
EXAMPLE
    compress(100000) returns '11_05'4
    compress(9993330) returns '93_33_01'
    compress(5640000) returns '61_51_41_04'
'''

from itertools import groupby

def compress(number_to_compress):
    # initialise list
    compressed_list = []
    for key, group in groupby(str(number_to_compress)):
        # save in list
        compressed_list.append((key + str(len(list(group)))))

    # convert list to string
    compressed_str = '_'.join(compressed_list)

    # print results
    print('Number to compress is {}'.format(number_to_compress))
    print('After compression... {}'.format(compressed_str))
    
    return compressed_str

# run test 1 
print('Test 1'.center(40,'-'))
number_to_compress = 100000
result_str = compress(number_to_compress)
if result_str == '11_05':
    print('Test passed')
else:
    print('Test failed')

# run test 2
print('Test 2'.center(40,'-'))
number_to_compress = 9993330
result_str = compress(number_to_compress)
if result_str == '93_33_01':
    print('Test passed')
else:
    print('Test failed')

# run test 3
print('Test 3'.center(40,'-'))
number_to_compress = 5640000
result_str = compress(number_to_compress)
if result_str == '51_61_41_04':
    print('Test passed')
else:
    print('Test failed')
