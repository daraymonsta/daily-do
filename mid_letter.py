'''
PURPOSE
    Function to return the middle letter of a string.
    
EXAMPLE
    mid("abc") should return "b" and mid("aaaa") should return ""
'''

def mid(input_str):
    # get string length
    input_str_len = len(input_str)
    
    # if number is odd, then find middle letter
    
    # get middle letter position
    middle_letter_pos = ((input_str_len-1) / 2)
    
    # check if the decimal part is zero
    # (if true if it's even and has a middle letter)
    if middle_letter_pos %1 == 0:
        middle_letter = input_str[int(middle_letter_pos)]
        print('Middle letter is {}'.format(middle_letter))
        return middle_letter
    else:
        print('There is no middle letter')
        return ""
    
input_str = "aBcDe"
mid(input_str)
