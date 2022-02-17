'''
PURPOSE
    Analyze a string to check if it contains two of the same letter
    in a row.  Your function must return True if there are two identical 
    letters in a row in the string, and False otherwise.
EXAMPLE
    The string "hello" has l twice in a row, while the string "nono"
    does not have two identical letters in a row.
'''

def double_letters(input_str):
    print('String: {}'.format(input_str))
    
    # load in two letters at a time in for loop
    for x in range(len(input_str)):
        
        # check there are still two letters left to grab
        if x+1 != len(input_str):
            
            # get two letters
            two_letters_str = input_str[x] + input_str[x+1]
            
            # check for matching letters
            if two_letters_str[0] == two_letters_str[1]:
                print('This pair of letters match: {}'.format(two_letters_str))
                return True
                break
    
    # if function actually makes it out of the loop without breaking
    # no double letters have matched
    print('String does not contain two of the same letter in a row')
    return False

input_str = "hello"
# run the function
double_letters(input_str)
