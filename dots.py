'''
PURPOSE
    Takes a string and adds "." in between each letter.
    Can also remove the "." between each letter.

EXAMPLE
    Calling add_dots("test") should return the string "t.e.s.t".
    Calling remove_dots("t.e.s.t") should return "test".
    calling remove_dots(add_dots(string)) should return back the 
    original string.

WRITTEN BY Ramon Rossi
'''

def add_dots(input_str):
    ''' Add a dot after each letter except the last letter '''
    temp_str = ""
    
    # loop through each letter in input_str
    for x in range(len(input_str)):
        
        # don't add dot after last letter, so
        # check if we are doing the last letter
        if x == (len(input_str)-1):
            print('This is the last letter, {}'.format(input_str[x]))
            temp_str = temp_str + input_str[x]
        else:
            temp_str = temp_str + input_str[x] + '.'
            print(input_str[x])
    
    return temp_str

def remove_dots(input_str):
    ''' Use replace function to replace all dots with nothing '''
    return input_str.replace('.','')

input_str = "bubble"
added_dots_str = add_dots(input_str)

# write test 1
print('\n')
print('Test 1 results - adding dots'.center(40,'-'))
print('Returned string = {}'.format(added_dots_str))
if added_dots_str == "b.u.b.b.l.e":
    print('Test passed')
else:
    print('Test failed')

removed_dots_str = remove_dots(input_str)

# write test 2
print('\n')
print('Test 2 results - removing dots'.center(40,'-'))
print('Returned string = {}'.format(removed_dots_str))
if removed_dots_str == "bubble":
    print('Test passed')
else:
    print('Test failed')
