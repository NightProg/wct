"""
Usage:
    wct (s | d) (~ | / | <path>) <regex>

Commands:
    s   Allows you to perform a search
    d   Allows to find and delete the corresponding elements (after confirmation)

Options:
    -f, --faster    Allows wct to go faster

"""
import sys, time

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

        # starts counting
        start_time = time.time()
        explorer.explorer(path, pattern)

        # excavation statistics
        print(f"\n{explorer.get_statistics()}")
        
        for item in explorer.get_target_paths():
            print(f"~ {item}")
        
        # displays the execution time
        print(f"\n[   {time.time() - start_time} seconds.   ]")
    
    elif args['d']:
        sys.exit("The 'd' command is currently unusable.")
