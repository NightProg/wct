import time, argparse

from src.module.explorer import Explorer
from src.colors import bcolors


if __name__ == "__main__":

    # COMMAND MODEL: wct <path> <pattern> [-c CHILD | --child CHILD]

    # Parser
    parser = argparse.ArgumentParser(prog="wct", description="Search and Moderation Wizard for the Computer Tree")
    parser.add_argument("path", type=str, help="Corresponds to the path where the search should start")
    parser.add_argument("pattern", type=str, help="Corresponds to the required motif")

    # Options group
    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument("-c","--child", type=int, default=None, help="Limits the search depth in number of children")

    args = parser.parse_args()
    print(args)

    if args:
        path = args.path
        pattern = args.pattern
        child = args.child
        explorer = Explorer()

        # starts count
        start_time = time.time()

        explorer.explorer(path, pattern)
        print(f"\n{explorer.get_statistics()}")
        
        for item in explorer.get_target_paths():
            sliced_item = item.split("/")
            last_elem = bcolors.GREEN + sliced_item[-1] + bcolors.RESET
            complete_item = '/'.join(sliced_item[:-1], last_elem)

            print(f"~ {complete_item}")
        
        # displays the execution time
        print(f"\n[   {time.time() - start_time} seconds   ]")