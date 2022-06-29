import sys
import src.search as search



if sys.argv[1] == "-s":  # python run.py -s ...
    print(search.searching(sys.argv))

else:
    print(f"\"{' '.join(sys.argv[1:])}\" is not recognized.")  # "a b c d" is not recognized.
