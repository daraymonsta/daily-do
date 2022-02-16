'''
PURPOSE
The function capital_indexes takes a single parameter, which is a string.
It returns a list of all the indexes in the string that have capital letters.

EXAMPLE
Calling capital_indexes("HeLlO") should return the list [0, 2, 4].
'''

def capital_indexes(input_str):
    try:
        input_str_len = len(input_str)
        # initialise list
        index_list = []
    
        # loop through each character
        for x in range(input_str_len):
          # check whether the character is a capital
          if input_str[x].isupper():
              # uncomment this line to manually check the string's capitals
              # print('character {} is a capital ({})'.format(x, input_str[x]))
              index_list.append(x)
        return index_list
        
    except TypeError:
        print('ERROR Input must be a string')
        
    except Exception as e:
        print("ERROR", e.__class__, "occurred.")
    
# get input string
input_str = "HeLlO"

# submit string to function
capital_index_list = capital_indexes(input_str)

# print capital_index_list if not empty
if capital_index_list:
    print(capital_index_list)
    
