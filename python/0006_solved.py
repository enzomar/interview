"""@package docstring
# 0005
## Attention point

## Solution Explanation

Most to least efficient: join, +
"""
import cProfile
import random
import string

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

def str_plus(input_list):
    s = str()
    for i in input_list:
        s += i
    return s


def str_join(input_list):
    return ''.join(input_list)


def concat(input_str):
    cProfile.run('str_join(input_str)')
    cProfile.run('str_plus(input_str)')

input_str = random_char(100000)
concat(input_str)