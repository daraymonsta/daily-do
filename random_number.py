'''
PURPOSE
    The function random_number(), will generate a random integer between
    1 and 100, both inclusive, and return it.

EXAMPLE
    Calling random_number() some times might first return 42, then 63, then 1
'''

import random
def random_number():
    return random.randint(1, 100)
    
print('Generating a random number between 1 and 100...')
# run the function & print it to the screen
print(random_number())
