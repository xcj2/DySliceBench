def examC():
    N, M = LI()
    A = [I() for _ in range(M)]
    A.append(N+1)
    fib = [1]*(N+2)
    for i in range(1,N):
        fib[i+2] = fib[i+1] + fib[i]
    fib[0] = 0
#    print(fib)
    ans = fib[A[0]]%mod
    for i in range(M):
        ans *= fib[A[i+1]-A[i]-1]
        ans %=mod
    print(ans)
    return

def examD():
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
inf = float('inf')

if __name__ == '__main__':
    examC()
