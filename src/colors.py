class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m' # RESET COLOR

    @staticmethod
    def print_red(text):
        print(bcolors.RED + str(text) + bcolors.RESET)
    
    @staticmethod
    def print_yellow(text):
        print(bcolors.YELLOW + str(text) + bcolors.RESET)
    
    @staticmethod
    def print_green(text):
        print(bcolors.GREEN + str(text) + bcolors.RESET)
    
    @staticmethod
    def print_blue(text):
        print(bcolors.BLUE + str(text) + bcolors.RESET)
