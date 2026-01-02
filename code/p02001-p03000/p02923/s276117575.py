from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

n = inp()
Hlist = inpl()

maxJ = 0
temp = 0
for i in range(len(Hlist)-1):
    if Hlist[i+1]<=Hlist[i]:
        temp+=1
    else:
        if temp > maxJ: maxJ = temp
        temp = 0

print(max(maxJ,temp))