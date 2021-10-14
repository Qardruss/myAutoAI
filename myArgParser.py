import sys
from typing import Any

def get_args() -> list:
    return sys.argv[1:]

def get_last_arg():
    try:
        return get_args()[-1]
    except IndexError:
        return None

def in_args(string: str) -> tuple:
    if string in get_args():
        for i in range(len(get_args())):
            if get_args()[i] != string:
                pass
            else:
                index = i
        return True, index,string
    else:
        return False, None,string

