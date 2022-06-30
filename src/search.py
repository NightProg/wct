import os, sys
from .module import username, ignore_analysis as ignore


class Search:
    def __init__(self, argv_list, username):
        self.argv_list = argv_list
        self.username = username

    def explorer(self):
        return "Dogo Yeb !"

    def search(self):
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
        else:
            print(f"\"{sys.argv[2]}\" is not recognized.")  # "--test" is not recognized.

