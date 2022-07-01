import os, sys
from .module import username, ignore_analysis as ignore
from .module import explorer


def search(argv_list, username):
    if self.argv_list[2] == "--root":
        os.chdir('../')
        return self.explorer()
    
    elif self.argv_list[2] == "--session":
        return self.explorer()

    elif self.argv_list[2] == "--anywhere":
        session = self.explorer()

        os.chdir('../')
        root = self.explorer()

        return session, root

