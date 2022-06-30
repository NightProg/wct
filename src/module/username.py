import os


def get_username():
    """ allows us to retrieve the username of our user on his machine """

    os.chdir('/home/')
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

    return str(username)
