def examB():
    N = I(); P = [I() for _ in range(N)]
    d = defaultdict(int)
    for i in range(N):
        d[P[i]] = d[P[i]-1]+1
    ans = N-max(d.values())
    d = defaultdict(int)
    for i in range(N-1,-1,-1):
        d[P[i]] = d[P[i]+1]+1
    ans = min(ans,N-max(d.values()))
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examB()
