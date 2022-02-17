'''
WRITTEN BY Ramon Rossi
PURPOSE
    Count the number of syllables in a string which is broken into
    syllables with hyphens.
EXAMPLE
    The call count("ho-tel") should return 2.
'''

def count(input_str):
    # count the number of hyphens and add one (for the first syllable)
    num_syllables = input_str.count("-") + 1
    print('Original string: {}'.format(input_str))
    print('Number of syllables: {}'.format(num_syllables))
    return num_syllables



# setup test 1
input_str = "ho-tel"
num_syllables = count(input_str)
print('Test 1'.center(40,'-'))
if num_syllables == 2:
    print('Test passed\n')
else:
    print('Test failed\n')
    
# setup test 2
input_str = "met-a-phor"
num_syllables = count(input_str)

print('Test 2'.center(40,'-'))
if num_syllables == 3:
    print('Test passed\n')
else:
    print('Test failed\n')
