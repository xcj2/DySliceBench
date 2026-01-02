import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

#from math import gcd
from functools import reduce

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    return gcd(r, b)

def gcd_list(numbers):
    return reduce(gcd, numbers)

K = ii()
ans = 0

memo = dp3(-1, K+1, K+1, K+1)

for i in range(1, K+1):
    for j in range(i+1, K+1):
        for k in range(j+1, K+1):
            ans += gcd_list([i, j, k])*6

for i in range(1, K+1):
    for j in range(1, K+1):
        if i!=j:
            ans += gcd_list([i, i, j])*3

for i in range(1, K+1):
    ans += gcd_list([i, i, i])


print(ans)