from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()
ABs = []
for _ in range(N):
    A,B = inpl()
    ABs.append([A+B,A,B])

ABs.sort(reverse=True)
t = a = 0

for i,[AB,A,B] in enumerate(ABs):
    if i%2 == 0:
        t += A
    else:
        a += B

print(t-a)
