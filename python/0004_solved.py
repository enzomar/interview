"""@package docstring
# 0004
## Attention point
Locating and avoiding bottlenecks is often pretty worthwhile. 
A lot of coding for efficiency comes down to common sense - in the example above it's obviously quicker to sort a list if it's a smaller list, so if you have the choice of filtering before a sort it's often a good idea. 
The less obvious stuff can still be located through use of the proper tools. 
It's good to know about these tools.

## Solution Explanation
Most to least efficient: f2, f1, f3. To prove that this is the case, you would want to profile your code. 
Python has a lovely profiling package that should do the trick.
"""

import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')