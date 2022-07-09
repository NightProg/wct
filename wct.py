import time, argparse

from src.module.explorer import Explorer
from src.colors import bcolors


if __name__ == "__main__":

    # COMMAND MODEL: wct <path> <pattern> [-d | --delete]

    # Parser
    parser = argparse.ArgumentParser(prog="wct", description="Search and Moderation Wizard for the Computer Tree")
    parser.add_argument("path", type=str, help="Corresponds to the path where the search should start")
    parser.add_argument("pattern", type=str, help="Corresponds to the required motif")

    # Options group
    options_group = parser.add_mutually_exclusive_group()
    options_group.add_argument("-d","--delete", action="store_true", help="Allows deletion at the end of the search (after confirmation)")

    args = parser.parse_args()
    print(args)

    if args:
        path = args.path
        pattern = args.pattern
        explorer = Explorer()

        # starts count
        start_time = time.time()

        explorer.explorer(path, pattern)
        print(f"\n{explorer.get_statistics()}")
        
        for item in explorer.get_target_paths():
            sliced_item = item.split("/")
            last_elem = bcolors.GREEN + sliced_item[-1] + bcolors.RESET
            sliced_item[-1] = last_elem
            complete_item = '/'.join(sliced_item)

            if args.delete:
                target_paths = explorer.get_target_paths()
                print(f"{target_paths.index(item)} ~ {complete_item}")
            else:
                print(f"~ {complete_item}")
        
        # displays the execution time
        print(f"\n[   {time.time() - start_time} seconds   ]")

        if args.delete:
            saved = input(f"""{bcolors.RED}
Using the index, write the individual items you do not
want to delete separated by commas.
Otherwise, enter <DE> to delete everything or <Enter> to exit.
{bcolors.RESET}""")

            if saved == "":
                quit()

            elif saved == "DE":
                print("DE")

            else:
                print(f"{bcolors.RED}/!\ Your entry is not correct /!\{bcolors.RESET}")
                # Here
