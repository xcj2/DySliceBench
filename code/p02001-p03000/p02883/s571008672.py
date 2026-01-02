
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
FF = inpl()

AA.sort()
FF.sort(reverse=True)


def solve(x):
    k = 0
    for i in range(N):
        A,F = AA[i],FF[i]
        k += max(0,A - (x//F))
    return k <= K

OK = 10**18
NG = -1

while OK - NG > 1:
    mid = (NG+OK)//2
    if solve(mid):
        OK = mid
    else:
        NG = mid

print(OK)
