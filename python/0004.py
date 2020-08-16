"""@package docstring
# 0004
## Description
Place the following functions below in order of their efficiency. 
They all take in a list of numbers between 0 and 1. 
The list can be quite long. An example input list would be [random.random() for i in range(100000)]. 
How would you prove that your answer is correct?
## Hints
- Displays knowledge of basic operating system interaction stuff
- Recursion is hella useful

"""


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]