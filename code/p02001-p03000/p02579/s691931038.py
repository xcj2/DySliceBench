import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write(' '.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
from decimal import Decimal
#from fractions import Fraction
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9)+7


h,w=mdata()
ch,cw=mdata()
dh,dw=mdata()
ch,cw,dh,dw=ch-1,cw-1,dh-1,dw-1
S=[data() for i in range(h)]
steps=[(0,1),(1,0),(-1,0),(0,-1)]
dist=[[INF]*w for i in range(h)]
dist[ch][cw]=0

queue = deque()
queue.append((ch, cw))
while queue:
    u, v = queue.popleft()
    d=dist[u][v]
    for i in range(-2, 3):
        for j in range(-2, 3):
            if 0 <= u + i < h and 0 <= v + j < w and S[u + i][v + j] == '.':
                if (i,j) in steps:
                    if d < dist[u+i][v+j]:
                        dist[u+i][v+j] = d
                        queue.appendleft((u+i,v+j))
                else:
                    if 1 + d < dist[u + i][v + j]:
                        dist[u + i][v + j] = 1 + d
                        queue.append((u + i, v + j))


if dist[dh][dw]!=INF:
    out(dist[dh][dw])
else:
    out(-1)
