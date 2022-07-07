import sys

from docopt import docopt
from src.module.explorer import Explorer


doc = """
Usage:
    wct (s | d) (~ | / | <path>) <regex>

Commands:
    s    Allows you to perform a search
    d    Allows to find and delete the corresponding elements (after confirmation)

"""

if __name__ == "__main__":
    args = docopt(doc, version="0.0.1")
    print(args)
    
    if args['s']:
        if args['~']: path = "~"
        elif args['/']: path = "/"
        elif args['<path>']: path = args['<path>']
        pattern = args['<regex>']

        # DEBUG
        # print(path)
        # print(pattern)

        explorer = Explorer()
        explorer.explorer(path, pattern)
        print(f"\n\n{explorer.get_target_paths()}")
    
    elif args['d']:
        sys.exit("The 'd' command is currently unusable.")
