'''
WRITTEN BY Ramon Rossi

PURPOSE
    The function named triple_and takes three parameters and returns True only if
    they are all True and False otherwise.
'''

def triple_and(bool1, bool2, bool3):
    if bool1 and bool2 and bool3:
        return True
    else:
        return False

# run test 1
result_bool = triple_and(True, True, True)
if result_bool:
    print('Test passed')
else:
    print('Test failed')