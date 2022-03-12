'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function named convert that takes a list of numbers as its only parameter and
    returns a list of each number converted to a string.

EXAMPLE
    The call convert([1, 2, 3]) should return ["1", "2", "3"].
'''

def convert(list_of_num):
    return [str(x) for x in list_of_num]

# run test 1
list_of_num = [1,2,3]
list_of_str = convert(list_of_num)
print(list_of_str)
if list_of_str == ["1", "2", "3"]:
    print('Test passed')
else:
    print('Test failed')