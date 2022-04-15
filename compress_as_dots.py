'''
WRITTEN BY Ramon Rossi
 
PURPOSE
    The function compress() accepts as input parameter a number to
    compress.  The functions returns a string of the compressed digits.
    To compress the number, each digit is stored along with dots for 
    the number of times that digit repeats.
    
EXAMPLE
    compress(1000040000) returns '1.0....4.0....'
    compress(20000000) returns '2.......'
    compress(123456) returns '1.2.3.4.5.6.'
'''

from itertools import groupby

def compress(number_to_compress):
    # initialise list
    compressed_list = []
    for key, group in groupby(str(number_to_compress)):
        # save in list
        compressed_list.append((key + str('.' * len(list(group)))))

    # convert list to string
    compressed_str = ''.join(compressed_list)

    # print results
    print('Number to compress is {}'.format(number_to_compress))
    print('After compression: {}'.format(compressed_str))
    
    return compressed_str

# run test 1 
print('Test 1'.center(40,'-'))
number_to_compress = 1000040000
result_str = compress(number_to_compress)
if result_str == '1.0....4.0....':
    print('Test passed')
else:
    print('Test failed')

# run test 2
print('Test 2'.center(40,'-'))
number_to_compress = 20000000
result_str = compress(number_to_compress)
if result_str == '2.0.......':
    print('Test passed')
else:
    print('Test failed')

# run test 3
print('Test 3'.center(40,'-'))
number_to_compress = 123456
result_str = compress(number_to_compress)
if result_str == '1.2.3.4.5.6.':
    print('Test passed')
else:
    print('Test failed')