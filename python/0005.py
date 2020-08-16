"""@package docstring
# 0005
## Description
count letter occurence in a string
## Hints
- do not think as c/c++ developer in python 

"""

import string
import random

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def count_letter(input_string):
    print("TODO")


if __name__ == "__main__":
    input_list_str = random_char(10000)
    count_letter(input_list_str)
