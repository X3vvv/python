import sys
import os.path

def get_file_path():
    """
    Take path from command line's single argument, or
    ask user to enter the path. If path exists, return
    True and the path. return false and empty string
    otherwise.
    """
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = input("Enter the path of the file:\n")

    if os.path.exists(path):
        return True, path
    else:
        return False, ""
