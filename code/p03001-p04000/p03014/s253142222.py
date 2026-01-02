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
    H, W = LI()
    S = [SI() for _ in range(H)]
    width = [[0]*W for _ in range(H)]
    height = [[0]*W for _ in range(H)]
    for i in range(H):
        cur = 0; keep = []
        for j in range(W):
            if S[i][j]==".":
                cur +=1
                keep.append(j)
            else:
                for k in keep:
                    width[i][k] = cur
                cur = 0; keep = []
        if keep:
            for k in keep:
                width[i][k] = cur
    for j in range(W):
        cur = 0; keep = []
        for i in range(H):
            if S[i][j]==".":
                cur +=1
                keep.append(i)
            else:
                for k in keep:
                    height[k][j] = cur
                cur = 0; keep = []
        if keep:
            for k in keep:
                height[k][j] = cur
    ans = 0
    for i in range(H):
        for j in range(W):
            cur = width[i][j] + height[i][j]
            if ans<cur:
                ans = cur
    print(ans-1)
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
    examD()
