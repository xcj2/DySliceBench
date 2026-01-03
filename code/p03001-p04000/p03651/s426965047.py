def gcd(x, y):
    if y == 0:
        return x
    while y != 0:
        x, y = y, x % y
    return x
def examA():
    N, K = LI()
    A = LI()
    ans = "POSSIBLE"
    if max(A)<K:
        ans = "IMPOSSIBLE"
    cur = A[0]
    for i in range(1,N):
        cur = gcd(cur,A[i])
    if K%cur!=0:
        ans = "IMPOSSIBLE"
    print(ans)
    return

def examB():
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
    examA()
