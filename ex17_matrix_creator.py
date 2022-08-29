'''
WRITTEN BY Ramon Rossi
 
PURPOSE
    The Matrix function turns a string into
    a matrix.  Each row of the matrix is stored
    on a separate line. Each element of a row is
    separated by a space.
    
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
        print(matrix_list)
    

# testing
print('Test 1'.center(30, '-'))
check_value = [['3', '4'], ['5', '6'], ['8', '9']]
matrix_obj = Matrix("3 4\n5 6\n8 9")
test1_value = matrix_obj.matrix
if check_value == test1_value:
    print('Test passed')
else:
    print('Test failed')
