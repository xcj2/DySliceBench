def examC():
    N, x  = LI()
    A = LI()
    ans = 0
    cur = A[0]
    if A[0]>x:
        ans += A[0]-x
        cur = x
    for i in range(1,N):
        if cur+A[i]<=x:
            cur = A[i]
            continue
        ans += cur+A[i]-x
        cur = A[i]-(cur+A[i]-x)
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,inf
mod = 10**9 + 7
inf = 10**18

if __name__ == '__main__':
    examC()
