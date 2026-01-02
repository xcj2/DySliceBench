import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write('\n'.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
from decimal import Decimal
# from fractions import Fraction
# sys.setrecursionlimit(100000)
mod = 998244353
INF=float('inf')




def find(x):
    while Group[x] != x:
        x = Group[x]
    return x

def Union(x, y):
    if find(x) != find(y):

        if Nodes[find(x)] < Nodes[find(y)]:
            Nodes[find(y)] += Nodes[find(x)]
            Nodes[find(x)] = 0
            Group[find(x)] = find(y)

        else:
            Nodes[find(x)] += Nodes[find(y)]
            Nodes[find(y)] = 0
            Group[find(y)] = find(x)




n,m=mdata()
Group = [i for i in range(n + 1)]
Nodes = [1] * (n + 1)
for i in range(m):
    a,b=mdata()
    Union(a,b)
s=set()
for i in Group[1:]:
    s.add(find(i))
out(len(s)-1)