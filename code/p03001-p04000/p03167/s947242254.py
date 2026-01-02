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

    
def fun(A,n,m):
    dp = list2d(n,m,0)
    for i in range(1,n): #initialising reachable first row
        if A[i][0]== '.':
            dp[i][0] = 1
        else:
            break
    for j in range(1,m): #initialising reachable first column
        if A[0][j] == '.':
            dp[0][j] = 1
        else:
            break
    dp[0][0] = 1
    for i in range(1,n):
        for j in range(1,m):
            if A[i][j] == "#":
                dp[i][j] = 0
                continue
            if A[i-1][j] == '.':
                dp[i][j] += dp[i-1][j]
                dp[i][j] %= MOD
            if A[i][j-1] == '.':
                dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    return int(dp[n-1][m-1])
        
H,W = ilele()
A = []
for i in range(H):
    B = [*input()]
    A.append(B.copy())
print(fun(A,H,W))