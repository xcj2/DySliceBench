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
mod = int(1e9) + 7
INF=float('inf')

ans=0
cnt=0
for i in range(int(data())):
    d1,d2=mdata()
    if d1==d2:
        cnt+=1
    else:
        ans = max(ans, cnt)
        cnt=0
ans=max(ans,cnt)
if ans>2:
    out("Yes")
else:
    out("No")