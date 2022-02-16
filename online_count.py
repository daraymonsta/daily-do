'''
PURPOSE
    Count the number of people whose status is 'online' given
    a dictionary of people's online status.

EXAMPLE
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    
    In this case, the number of people online is 2.
'''

def online_count(statuses):
    print('METHOD 1 - convert dictionary to list first')
    # initialise int to store number of people online
    num_users_online = 0
    
    # convert dictionary to list so index can be referred to
    # in the loop through the values
    statuses_list = list(statuses.values())
    
    for x in range(len(statuses_list)):
        if statuses_list[x] == 'online':
            num_users_online += 1
    
    print('There are {} users online'.format(num_users_online))
    
    print('\nMETHOD 2 - loop through dictionary')
    # reset int to store number of people online
    num_users_online = 0
    
    for status in statuses:
        if statuses[status] == 'online':
            num_users_online += 1
    
    print('There are {} users online'.format(num_users_online))    
    
    return num_users_online

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

# call the function
num_users_online = online_count(statuses)
