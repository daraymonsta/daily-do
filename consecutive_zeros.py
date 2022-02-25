def consecutive_zeros(input_str):
    print('Question: How many consecutive zeros in {}?'.format(input_str))
    
    # loop through each character
    for x in range(len(input_str)):
        #print(input_str[x])
        
        # it's the first character
        if x == 0:
            prev_num = input_str[x]
            #print('first num is {}'.format(prev_num))
            if input_str[x] == "1":
                temp_counter = 0
            elif input_str[x] == "0":
                temp_counter = 1
            biggest_count = 0
        # it's not the first character
        else:
            this_num = input_str[x]
            #print('this number is {}'.format(this_num))
            #print('previous num is {}'.format(prev_num))
            
            # if it's a zero & the same as the last character
            if (this_num == prev_num) and (this_num == "0"):
                # add to count
                temp_counter += 1
                #print('added 1 to temp_counter')
            # if it's a zero but not the same as the last character
            elif (this_num != prev_num) and (this_num == "0"):
                temp_counter = 1
                #print('this is the first 0, temp_counter = 1')
            # if it's not a zero
            elif this_num == "1":
                # reset counter
                temp_counter = 0
                #print('reset temp_counter')
            
            # finally, we need to set this number to be the
            # the previous num for the next time in the loop
            prev_num = this_num
        
        #print('temp counter = {}'.format(temp_counter))
        
        # make sure biggest count is only set if there 
        # are more consecutive zeros than before
        if temp_counter > biggest_count:
            biggest_count = temp_counter
        elif temp_counter > 0 and biggest_count == 0:
            biggest_count = temp_counter
        
        #print('biggest count = {}'.format(biggest_count))
            
    print('Answer: {}'.format(biggest_count))
    
    return biggest_count

# run test 1
print('Test 1'.center(40,'-'))

input_str = "1001101000110"
num_consec_zeros = consecutive_zeros(input_str)

if num_consec_zeros == 3:
    print('Test passed')
else:
    print('Test failed')