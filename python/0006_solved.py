"""@package docstring
# 0005
## Attention point

## Solution Explanation

Most to least efficient: join, +
"""

def str_plus(input_list):
    s = str()
    for i in input_list:
        s += i
    return s


def str_join(input_list):
    return ''.join(input_list)