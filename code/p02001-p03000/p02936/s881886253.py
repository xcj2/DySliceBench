import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
#from math import floor, ceil
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
#inf = 10**17
#mod = 10**9 + 7

n,q=MI()
relation=[[] for i in range(n)]
for i in range(n-1):
    a,b=MI()
    a-=1
    b-=1
    relation[a].append(b)
    relation[b].append(a)
#print(relation)

nodes=[0]*n
for i in range(q):
    p,r=MI()
    p-=1
    nodes[p]+=r

Q=deque()
Q.append([-1,0])
#print(Q.popleft())

while Q:
    s,t=Q.popleft()
    for um in relation[t]:
        if um ==s:
            continue
        nodes[um]+=nodes[t]
        Q.append([t,um])
        
print(" ".join(map(str,nodes)))
    