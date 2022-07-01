import sys
import src.search as search
from src.module.params_verification import verification


verification(sys.argv)

if sys.argv[1] == "-s":  # python run.py -s ...
    username = search.username.get_username() 
    search.search(sys.argv, username)
