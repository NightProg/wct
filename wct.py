import time, argparse

from src.module.explorer import Explorer


if __name__ == "__main__":

    # COMMAND MODEL: wct <path> <pattern> [-c CHILD | --child CHILD]

    parser = argparse.ArgumentParser(prog="wct", description="Search and Moderation Wizard for the Computer Tree")
    parser.add_argument("path", type=str, help="Corresponds to the path where the search should start")
    parser.add_argument("pattern", type=str, help="Corresponds to the required motif")

    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument("-c","--child", help="Limits the search depth in number of children")

    subparsers = parser.add_subparsers(help='sub-command help')

    args = parser.parse_args()

    if args.path:
        path = args.path
        pattern = args.pattern
        explorer = Explorer()

        # starts count
        start_time = time.time()

        explorer.explorer(path, pattern)

        # excavation statistics
        print(f"\n{explorer.get_statistics()}")
        
        for item in explorer.get_target_paths():
            print(f"~ {item}")
        
        # displays the execution time
        print(f"\n[   {time.time() - start_time} seconds.   ]")