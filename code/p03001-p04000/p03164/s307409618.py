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
    
def knapsack(wts,P,N,W):
    if N==0 or W == 0:
        return 0
    dp = list2d(100,100001,1e10) #dp[item][val] = weight
    dp[0][0] = 0
    dp[0][P[0]] = wts[0]
    ##we have to minimize the weight
    for i in range(1,N):
        dp[i][0] = 0
        for j in range(1,100000+1):
            dp[i][j] = dp[i-1][j] # discarding current
            if P[i] <= j:
                dp[i][j] = min(wts[i] + dp[i-1][j - P[i]] , dp[i][j])
            
    #minimum weight
    for val in range(100000,-1,-1):
        if dp[N-1][val] <= W:
            return val #returning the val at maximum weight
    

N,W = ilele()
P = []
A = []
for i in range(N):
    a,b =ilele()
    A.append(a)
    P.append(b)
print(knapsack(A,P,N,W))
    