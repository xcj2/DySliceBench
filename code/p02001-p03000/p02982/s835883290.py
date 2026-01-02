from collections import defaultdict,deque, Counter
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

ans = 0
[n,d] = inpl()
Xmatrix = [inpl() for _ in range(n)]
npXmatrix = np.array(Xmatrix)
for i in range(n):
    for j in range(i+1,n):
        if is_square(((npXmatrix[i]-npXmatrix[j])**2).sum()):
            ans += 1
print(ans)