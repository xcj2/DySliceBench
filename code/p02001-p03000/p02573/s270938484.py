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


n,m=mdata()
Group = [i for i in range(n + 1)]
Nodes = [1] * (n + 1)

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

for i in range(m):
    x, y = mdata()
    Union(x, y)
d=dd(int)
for i in range(1,n+1):
    d[find(i)]+=1
out(max(d.values()))