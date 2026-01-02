import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

N = I()

def trial_division(n):
    d = defaultdict(int)
    while n%2 == 0:
        d[2] += 1
        n = n//2
    p = 3
    while p**2 <= n:
        while n%p == 0:
            d[p] += 1
            n = n//p
        p += 2
    if n != 1:
        d[n] += 1
    return d


d = trial_division(N)
ans = 0
for k in d.keys():
    ok = 0
    ng = 2*d[k]
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if mid*(mid+1) <= 2*d[k]:
            ok = mid
        else:
            ng = mid
    ans += ok

print(ans)