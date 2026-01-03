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


w,h,n=l()
r=[i for i in range(w+1)]
c=[i for i in range(h+1)]
for i in range(n):
    # print(r,c)
    a,b,x=l()
    if(x==1):
        r=r[br(r,a-1):]
    elif(x==2):
        r=r[:bl(r,a+1)]
    elif(x==3):
        c=c[br(c,b-1):]
    else:
        c=c[:bl(c,b+1)]
# print(r,c)
if(len(r)==0 or len(c)==0):
    print(0)
    exit()
print((max(r)-min(r))*(max(c)-min(c)))
