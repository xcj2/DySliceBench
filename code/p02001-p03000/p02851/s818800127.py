
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,K = inpl()
AA = inpl()

rAA = [0]
for a in AA:
    rAA.append(rAA[-1]+a)


AA = [(A+N-i)%K for i,A in enumerate(rAA)]


cnts = defaultdict(int)
ans = 0
for i,a in enumerate(AA):
    if i >= K:
        cnts[AA[i-K]] -= 1

    ans += cnts[a]
    cnts[a] += 1



print(ans)
