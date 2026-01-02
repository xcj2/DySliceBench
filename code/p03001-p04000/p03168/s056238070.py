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

    
def fun(A,N):
    dp = list2d(3000,3000,0)
    dp[0][0] = 1 - A[0]
    dp[0][1] = A[0]
    for i in range(1,N):
        for j in range(3000):
            #tails
            dp[i][j] += (1-A[i])*dp[i-1][j]
            #heads
            if j > 0:
                dp[i][j] += A[i]*(dp[i-1][j-1])
    ans = 0
    for i in range(N//2 + 1,3000):
        ans += dp[N-1][i]
    return ans
        
N = int(input())
A = list(map(float, input().split()))
print(fun(A,N))