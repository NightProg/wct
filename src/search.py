import os
from .module.explorer import explorer


def search(argv_list, username):
    """ drops the explorer where the user wants it according to the second screen of the command """

    if argv_list[2] == "--root":
        os.chdir('../')
        return explorer(argv_list[3])
    
    elif argv_list[2] == "--session":
        return explorer(argv_list[3])

    elif argv_list[2] == "--anywhere":
        session = explorer(argv_list[3])

        os.chdir('../')
        root = explorer(argv_list[3])

        return session, root

