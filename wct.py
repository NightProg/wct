"""
Usage:
    wct s <path> <regex>

Commands:
    s   Allows you to perform a search

Options:
    -p=<children>, --parent=<number>    Limits the search depth in number of children

"""
import sys, time

from docopt import docopt
from src.module.explorer import Explorer


if __name__ == "__main__":
    args = docopt(__doc__, version="0.0.1")
    print(args)
    
    if args['s']:
        path = args['<path>']
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
    
