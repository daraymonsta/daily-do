'''
WRITTEN BY Ramon Rossi

PURPOSE
    Imagine you're writing a tic-tac-toe game, where the board looks 
    like this:
    
    board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
    ]
    
    Imagine if your user enters "C1" and you need to see if there's an
    X or O in that cell on the board. To do so, you need to translate 
    from the string "C1" to row 0 and column 2 so that you can check 
    board[row][column].

    The function will get_row_col can translate from strings of length
    2 to a tuple (row, column). Name your function get_row_col; it
    should take a single parameter which is a string of length 2 
    consisting of an uppercase letter and a digit.
    
EXAMPLE
    Calling get_row_col("A3") should return the tuple (2, 0) because
    A3 corresponds to the row at index 2 and column at index 0 in the
    board.
'''

def get_row_col(position_str):
    print('Position input = {}'.format(position_str))
    # check position input is valid
    position_str_ok = validate_position_str(position_str)
    if position_str_ok:
        col = position_str[0]
        row = position_str[1]
        if col == 'A':
            col_index = 0
        elif col == 'B':
            col_index = 1
        elif col == 'C':
            col_index = 2
        else:
            print('Error: Invalid column')
    
        try:
            row_index = int(row) - 1
            if row_index > 2:
                print('Error: Invalid row')
        except:
            print('Error: Invalid row')
        
        print('row index = {}, column index = {}'.format(row_index, col_index))
        return (row_index, col_index)
        

def validate_position_str(position_str):
    try:
        if len(position_str) != 2:
            raise ValueError('Input is too long')
        if position_str[0].isalpha() == False:
            raise ValueError('First character is not a letter')
        if position_str[0].isupper() == False:
            raise ValueError('First character is not a capital')
        if position_str[1].isdigit() == False:
            raise ValueError('Second character is not a digit')
        else:
            if int(position_str[1]) > 3:
                raise ValueError('Second character is bigger than 3')
            if int(position_str[1]) < 1:
                raise ValueError('Second character is smaller than 1')
        return True
    except Exception as error:
        print('Error: ' + repr(error))
        return False

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

# test 1
print('Test 1'.center(40,'-'))
position_str = "C1"
position_tuple = get_row_col(position_str)
if position_tuple == (0, 2):
    print('Test passed')
else:
    print('Test failed')

# test 2
print('Test 2'.center(40,'-'))
position_str = "A3"
position_tuple = get_row_col(position_str)
if position_tuple == (2, 0):
    print('Test passed')
else:
    print('Test failed')