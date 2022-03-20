'''
WRITTEN BY Ramon Rossi

PURPOSE
    Consider the Fionacci sequence.  It is a sequence of natural numbers defined
    recursively as follows:
    * the first element is 0
    * the second is 1 
    * each next element is the sum of the previous two elements

    This function will sum all even elements of the Fibonacci sequence with values
    less than 1 million.  The function is called calculate() and prints the result
    to the console.

EXAMPLE
    calculate(1000000) will have the result 1089154.
'''

def calculate(limit):
    values_list = []
    x = 0
    
    # increment x by 1 until the Fibonacci number gets to the limit
    while(True):
        # the first element must be 0, and the second element must be 1
        if x == 0 or x == 1:
            values_list.append(x)
        # the rest of the elements adds the previous two values
        else:
            values_list.append(values_list[x-1]+values_list[x-2])
        
        # uncomment this line if need to see each Fibonacci number as its generated
        #print('Element {}, Fibonacci number is {}'.format(x, values_list[x]))
        
        # check if the Fibonacci number is at or past the limit
        if values_list[x] >= limit:
            # remove this last list item because its at or past the limit
            values_list.pop(x)
            break
        
        # increment x by 1
        x += 1
    
    # the values in the list are added if they are even    
    sum_of_even_values = sum([values_list[i] for i in range(len(values_list)) if values_list[i]%2 == 0])
    print(values_list)
    
    return sum_of_even_values

# run test 1 
print('Test 1'.center(40,'-'))
limit = 1000000
result = calculate(limit)
print('Sum of all even Fibonacci numbers up to {}: {}'.format(limit, result))
if result == 1089154:
    print('Test passed')
else:
    print('Test failed')