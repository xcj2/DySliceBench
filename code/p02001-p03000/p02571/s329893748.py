import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
from decimal import Decimal
# from fractions import Fraction
# sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9) + 7


s=data()
t=data()
ans=INF
for i in range(len(s)-len(t)+1):
    cnt=0
    for j in range(len(t)):
        if s[i+j]!=t[j]:
            cnt+=1
    ans=min(ans,cnt)
out(ans)