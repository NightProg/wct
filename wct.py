"""
Usage:
    wct (s | d) (~ | / | <path>) <regex>

Commands:
    s    Allows you to perform a search
    d    Allows to find and delete the corresponding elements (after confirmation)

"""
import sys

from docopt import docopt
from src.module.explorer import Explorer


if __name__ == "__main__":
    args = docopt(__doc__, version="0.0.1")
    
    if args['s']:
        if args['~']: path = "~"
        elif args['/']: path = "/"
        elif args['<path>']: path = args['<path>']

        pattern = args['<regex>']
        explorer = Explorer()
        explorer.explorer(path, pattern)

        print(f"{explorer.get_statistics()}\n")
        
        for item in explorer.get_target_paths():
            print(f"~ {item}")
    
    elif args['d']:
        sys.exit("The 'd' command is currently unusable.")
