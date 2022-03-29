'''
WRITTEN BY Ramon Rossi

PURPOSE
    The prime number is position one is 2.  The prime number in position
    two is 3.  The prime number is position three is 5.  This function is_prime()
    finds the prime number at any position. It accepts an integer as an argument 
    which is the position of the prime number to find.  It returns the prime
    number at that position.
    
EXAMPLE
    is_prime(100) will find the prime number at position 100 - it should return
    541.
'''

def is_prime(position_int):
    # 1 is not prime, so start with 2
    x = 2
    prime_num_list = []
    count_prime_num_position = 0
    
    while True:
        
        if x == 2:
            # add 2 to prime number list
            prime_num_list.append(x)
            count_prime_num_position += 1
        else:
            # check if x is prime by dividing by y
            for y in range(2, x):
                if x % y == 0:
                    #print('Not prime')
                    break
                
                if (y+1) == x:
                    #print('Prime')
                    prime_num_list.append(x)
                    count_prime_num_position += 1
                #print('divisor = {}'.format(y))
        
        # if found enough prime numbers, break the loop
        if count_prime_num_position == position_int:
            break
        x += 1
        
    print('Prime numbers up to position {}...'.format(position_int))
    print(prime_num_list)
    return prime_num_list[position_int-1]

# run test 1
print('Test 1'.center(40,'-'))

position_int = 3
result = is_prime(position_int)
print('The prime number at position {} is {}'.format(position_int, result))

if result == 5:
    print('Test passed\n')
else:
    print('Test failed\n')
    
# run test 2
print('Test 2'.center(40,'-'))

position_int = 100
result = is_prime(position_int)
print('The prime number at position {} is {}'.format(position_int, result))

if result == 541:
    print('Test passed\n')
else:
    print('Test failed\n')