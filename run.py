import sys
import src.search as search


if sys.argv[1] == "-s":  # python run.py -s ...
    print(search.get_argv_data(sys.argv))

else:
    print(f"\"{' '.join(sys.argv[1:])}\" is not recognized.")  # "a b c d" is not recognized.