class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m' # RESET COLOR

    @staticmethod
    def print_red(text):
        print(bcolors.RED + text + bcolors.RESET)
    
    @staticmethod
    def print_yellow(text):
        print(bcolors.YELLOW + text + bcolors.RESET)
    
    @staticmethod
    def print_green(text):
        print(bcolors.GREEN + text + bcolors.RESET)
    
    @staticmethod
    def print_blue(text):
        print(bcolors.BLUE + text + bcolors.RESET)