import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
#sys.setrecursionlimit(200000000)
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
ilele = lambda: map(int,input().split())
alele = lambda: list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
#def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
    
def fun(A,P,W,N):
    if N == 0 or W == 0:
        return 0
    dp = list2d(N+1,W+1,0)
    for i in range(1,N+1):
        for j in range(1,W+1):
            if A[i-1] <= j:
                dp[i][j] = max(dp[i-1][j] , P[i-1] + dp[i-1][j - A[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][W]
N,W = ilele()
P = []
A = []
for i in range(N):
    a,b =ilele()
    A.append(a)
    P.append(b)
print(fun(A,P,W,N))
    