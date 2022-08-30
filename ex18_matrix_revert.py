'''
WRITTEN BY Ramon Rossi
 
PURPOSE
    The Matrix function turns a string into
    a matrix.  Each row of the matrix is stored
    on a separate line. Each element of a row is
    separated by a space.
    
    Added for Exercise 18:
    The method __repr__ in the Matrix class
    converts the matrix back to it's Starting
    string
    
EXAMPLE
    matrix_obj = Matrix("3 4\n5 6\n8 9")
    matrix_obj.matrix
'''

class Matrix:
    # init method or constructor
    def __init__(self, input_str):
        row_list = input_str.split("\n")
        matrix_list = []
        for x in range(len(row_list)):
            matrix_list.append(row_list[x].split())
        self.matrix = matrix_list

    def __repr__(self):
        matrix_list = self.matrix
        row_list = []
        for x in range(len(matrix_list)):
            row_list.append(' '.join(map(str,matrix_list[x])))
        original_str = '\n'.join(map(str,row_list))
        return original_str
    

# test 1
print('Test 1'.center(30, '-'))
check_value = [['3', '4'], ['5', '6'], ['8', '9']]
print('Starting string')
starting_str = "3 4\n5 6\n8 9"
print(starting_str)
matrix_obj = Matrix(starting_str)
print('\nMatrix as a nested list')
print(matrix_obj.matrix)
test1_value = matrix_obj.matrix
if check_value == test1_value:
    print('Test passed')
else:
    print('Test failed')

# print break
print('\n')

# test 2
print('Test 2'.center(30, '-'))
print('Original string')
print(matrix_obj.__repr__())
if starting_str == matrix_obj.__repr__():
    print('Test passed')
else:
    print('Test failed')
