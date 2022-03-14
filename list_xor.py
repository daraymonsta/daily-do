'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function is named list_xor; it should take three parameters: n, list1 and list2.

    The function must return whether n is exclusively in list1 or list2.

    In other words, if n is in both lists or in none of the lists, return False. If n
    is in only one of the lists, return True.

EXAMPLE
    list_xor(1, [1, 2, 3], [4, 5, 6]) == True
    list_xor(1, [0, 2, 3], [1, 5, 6]) == True
    list_xor(1, [1, 2, 3], [1, 5, 6]) == False
    list_xor(1, [0, 0, 0], [4, 5, 6]) == False
'''

def list_xor(n, list1, list2):
    if n in list1 and n in list2:
        print('Found in both lists')
        return False
    elif n in list1 or n in list2:
        print('Found in one list only')
        return True
    else:
        print('Not found in either list')
        return False
    
    
# run test 1
print('Test 1'.center(40, '-'))
n = 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_bool = list_xor(n, list1, list2)
if result_bool:
    print('Test passed\n')
else:
    print('Test failed\n')

# run test 2
print('Test 2'.center(40, '-'))
n = 1
list1 = [0, 2, 3]
list2 = [1, 5, 6]
result_bool = list_xor(n, list1, list2)
if result_bool:
    print('Test passed\n')
else:
    print('Test failed\n')
    
# run test 3
print('Test 3'.center(40, '-'))
n = 1
list1 = [1, 2, 3]
list2 = [1, 5, 6]
result_bool = list_xor(n, list1, list2)
if not result_bool:
    print('Test passed\n')
else:
    print('Test failed\n')
    
# run test 4
print('Test 4'.center(40, '-'))
n = 1
list1 = [0, 0, 0]
list2 = [4, 5, 6]
result_bool = list_xor(n, list1, list2)
if not result_bool:
    print('Test passed\n')
else:
    print('Test failed\n')