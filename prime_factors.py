'''
WRITTEN BY Ramon Rossi

PURPOSE
    We can break down a composite number into prime factors.  For example:
        15 = 3 x 5 
        36 = 2 x 2 x 3 x 3 
        48 = 2 x 2 x 2 x 2 x 3 
    
    The function calculate() takes a natural number as an argument and returns a list
    containing the prime factorization of that number.
    
EXAMPLE 
    calculate(15) returns the list [3, 5]
    calculate(36) returns the list [2, 2, 3, 3]
    calculate(48) returns the list [2, 2, 2, 2, 3]
'''

def calculate(temp_int):
    # initialise variables
    prime_num_list = []
    prime_factors_list = []

    # get prime numbers until you reach temp_int
    for x in range(2, temp_int):
        #print('Checking {}'.format(x))
        not_prime_bool = False
        for i in range (2, x-1):
            # if has a remainder, it's not prime
            if x%i == 0:
                #print('Divided evenly by {} so not prime'.format(i))
                not_prime_bool = True
            
        if not_prime_bool == False:
            # add to list of prime numbers
            prime_num_list.append(x)
                
    #print('List of prime numbers...')
    #print(prime_num_list)    
    
    quotient = temp_int
    while quotient != 1:
        
        # loop possible divisors
        for d in prime_num_list:
            # check can divide by d
            if quotient%d == 0:
                #print('Divided by {} with no remainder'.format(d))
                prime_factors_list.append(d)
                quotient = quotient/d
                break
    
    print('Prime factorization for {}...'.format(temp_int))
    print(prime_factors_list)
    
    return prime_factors_list

# run test 1
print('Test 1'.center(40, '-'))
a_number = 15
result = calculate(a_number)
if result == [3, 5]:
    print('Test passed')
else:
    print('Test failed')
    
# run test 2
print('Test 2'.center(40, '-'))
a_number = 36
result = calculate(a_number)
if result == [2, 2, 3, 3]:
    print('Test passed')
else:
    print('Test failed')

# run test 3 
print('Test 3'.center(40, '-'))
a_number = 48
result = calculate(a_number)
if result == [2, 2, 2, 2, 3]:
    print('Test passed')
else:
    print('Test failed')