def num():
    return int(input())
def nums():
    return list(map(int,input().split()))

import itertools as iter
import math
import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

N,M = nums()
AC = set()
WA = {}
for _ in range(M):
    pi,si = input().split()
    if si == "AC":
        AC.add(pi)
    else:
        if not (pi in WA.keys()) and not pi in AC:
            WA[pi] = 1
        else:
            if not (pi in AC):
                WA[pi] += 1

for problem in WA.keys():
    if not (problem in AC):
        WA[problem] = 0
ACnum = len(AC)
WAnum = sum(WA.values())
print(ACnum,WAnum)

