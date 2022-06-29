import os
from . import ignore_analyser as ignore


def searching(argv_params):
    os.chdir('/home/')
    
    # this part of the program allows to register the username of our user
    # to be able to access his whole file tree 
    users = {}

    for user in os.listdir():
        if user == ".directory":
            continue
        i = 1
        users[str(i)] = user
        i += 1

    for key, user in users.items():
        print(f"[{key}] : {user}")
    
    user_id = input('Who are you ? ')

    try:
        username = users[user_id]
    except:
        print(f"\nNo user associated with key {user_id}")
        quit()
    
    return f"Welcome user {users[user_id]} !" 

