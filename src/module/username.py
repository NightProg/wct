import os


def get_username():
    current_directory = os.getcwd()
    current_directory_slicing = current_directory.split("/")
    username_index = current_directory_slicing.index("home") + 1
    
    return current_directory_slicing[username_index]

