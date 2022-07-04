import sys
import src.search as search

from src.module.params_verification import verification
from src.module.username import get_username


verification(sys.argv)

if sys.argv[1] == "-s":  # python run.py -s ...
    username = get_username() 
    result = search.search(sys.argv, username)
    print(result)
