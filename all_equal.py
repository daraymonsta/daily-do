'''
WRITTEN BY Ramon Rossi
PURPOSE
    The function named all_equal that takes a list and checks whether all elements
    in the list are the same.
    
EXAMPLE
    Calling all_equal([1, 1, 1]) should return True.
'''

def all_equal(input_list):
    print('Input list is {}'.format(input_list))
    #print('Input list without the 1st item is {}'.format(input_list[1:]))

    # loop through each element of the list starting with the second item
    for x in input_list[1:]:
        #print('Current item: {}'.format(x))
        # compare each list item with the first item
        if x != input_list[0]:
            print('Result: Not all elements in the list are the same')
            return False
            break
    
    print('Result: All elements in the list are the same')
    return True

# run test
print('Test 1'.center(40,'-'))
input_list = [1, 1, 1]
result = False
result = all_equal(input_list)

if result:
    print('Test passed\n')
else:
    print('Test failed\n')
