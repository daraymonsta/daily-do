'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function named zap takes two parameters, a and b. These are lists.
    
    The function should return a list of tuples. Each tuple should contain one item 
    from the a list and one from b.

    Assume a and b have equal lengths.

EXAMPLE
    zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
    )
    
    should return:
    
    [(0, 5),
    (1, 6),
    (2, 7),
    (3, 8)]
'''

def zap(a, b):
    # initialise result list
    result_list = []
    
    # one-line method:
    # loop through a, appending to result_list with each iteration
    [result_list.append((a[x], b[x])) for x in range(len(a))]

    # longer way to do the same thing:
    '''
    for x in range(len(a)):
        result_list.append((a[x], b[x]))
    '''
    return result_list

# run test 1
a = [0, 1, 2, 3]
b = [5, 6, 7, 8]
result_list = zap(a, b)
print(result_list)
if result_list == [(0, 5),(1, 6),(2, 7),(3, 8)]:
    print('Test passed')
else:
    print('Test failed')