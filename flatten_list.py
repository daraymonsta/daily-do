'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function takes a list of lists and flattens it into a 
    one-dimensional list.

EXAMPLE
    Calling flatten([[1, 2], [3, 4]]) should return the list
    [1, 2, 3, 4]
'''

def flatten(tall_list):
    flatter_list = []

    # loop through the elements in the non-flattened list
    for x in range(len(tall_list)):
        
        # loop through the sub-elements of the non-flattened list
        for y in range(len(tall_list[x])):
            # add each list sub-element to a flat list
            flatter_list.append(tall_list[x][y])

    print(flatter_list)
    return flatter_list

# test the function works
tall_list = [[1, 2], [3, 4]]
flatter_list = flatten(tall_list)
if flatter_list == [1, 2, 3, 4]:
    print('Test passed')
else:
    print('Test failed')
