"""@package docstring
# 0005
## Attention point

## Solution Explanation

Most to least efficient: dict_default, dict_try, dict_if, dict_get, dict_setd
"""



from collections import defaultdict
import string
import random

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))



def dict_if(input_list):
    wdict = dict()
    for word in input_list:
        if word not in wdict:
            wdict[word] = 0
        wdict[word] += 1


def dict_try(input_list):
    wdict = dict()
    for word in input_list:
        try:
            wdict[word] += 1
        except KeyError:
            wdict[word] = 1


def dict_get(input_list):
    wdict = dict()
    for word in input_list:
        wdict[word] = wdict.get(word, 0) + 1


def dict_setd(input_list):
    wdict = dict()
    for word in input_list:
        wdict.setdefault(word, 0)
        wdict[word] += 1


def dict_default(input_list):
    wdict = defaultdict(int)

    for word in input_list:
        wdict[word] += 1

