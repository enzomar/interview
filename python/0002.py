"""@package docstring
# 0002
## Description
Looking at the below code, write down the final values of A0, A1, ...An.

## Hints
- List comprehension is a wonderful time saver and a big stumbling block for a lot of people
- If you can read them, you can probably write them down
- Some of this code was made to be deliberately weird. You may need to work with some weird people

"""


A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]