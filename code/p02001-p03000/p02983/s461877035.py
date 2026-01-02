import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from math import *
# import math
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
# sys.setrecursionlimit(int(pow(10, 2)))
# sys.stdin = open("input.txt", "r")
# sys.stdout = open("output.txt", "w")
mod = int(pow(10, 9) + 7)
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def l(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]





# @lru_cache(None)


    


L,r=l()

if(r-L>=2019):
    print(0)
    exit()
if(r-L<2019 and 0 in [i%2019 for i in range(L,r+1)]):
    print(0)
    exit()
x=[(i*j)%2019 for i in range(L,r+1) for j in range(i+1,r+1)]
print(min(x))

