# -*- coding: utf-8 -*-

################ DANGER ################
test = ""
#test = \
"""
5 2 4
ans 1
"""

"""
5 2 3
ans 2
"""

"""
5 3 4
ans 2
"""

"""
7 2 5
ans 3, not 4 
"""
########################################
test = list(reversed(test.strip().splitlines()))
if test:
    def input2():
        return test.pop()
else:
    def input2():
        return input()
########################################  
    
n, a, b = map(int, input2().split())

def roundup(n, d):
    if n % d:
        return n // d + 1
    else:
        return n // d


if (b - a) % 2 == 0:
    print((b - a) // 2)
    
else:
    if (b - 1) < (n - a):
        print((a - 1) + roundup((b - a), 2))
            
    else:
        print((n - b) + roundup((b - a), 2))
        