'''
WRITTEN BY Ramon Rossi
PURPOSE
    Two strings are anagrams if you can make one from the other 
    by rearranging the letters. The function named is_anagram takes
    two strings as its parameters, returning True if the strings are
    anagrams and False otherwise.

EXAMPLE
    The call is_anagram("typhoon", "opython") should return True 
    while the call is_anagram("Alice", "Bob") should return False.
'''

def str_to_sorted_list(temp_str):
    # convert str to list of letters
    temp_list = list(temp_str)
    # sort list in alphabetical order
    temp_list.sort()
    return temp_list

def is_anagram(str1, str2):
    # print the original strings
    print('First string: {}'.format(str1))
    print('Second string: {}'.format(str2))
    
    # convert each string into a list of letters, then sort the 
    # list alphabetically 
    str1_sorted_list = str_to_sorted_list(str1)
    str2_sorted_list = str_to_sorted_list(str2)

    # compare whether the sorted lists of letters are the same
    if str1_sorted_list == str2_sorted_list:
        print('They are anagrams')
        return True
    else:
        print('They are not anagrams')
        return False

def run_test(str1,str2,should_anagram_be_true):
    whether_anagram = is_anagram(str1, str2)
    if whether_anagram == should_anagram_be_true:
        print('Test passed\n')
    else:
        print('Test failed\n')

# test 1
str1 = "typhoon"
str2 = "opython"
run_test(str1,str2,True)

# test 2
str1 = "Alice"
str2 = "Bob"
run_test(str1,str2,False)

