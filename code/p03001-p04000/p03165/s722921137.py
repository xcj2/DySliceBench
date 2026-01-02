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
      
def fun(A,B,m,n,dp):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp
                
def longestsub(A,B):
    m = len(A)
    n = len(B)
    if m==0 or n==0:
        return ""
    temp = [0]*(n+1)
    dp = [temp.copy() for i in range(m+1)]
    d = fun(A,B,m,n,dp)
    i= m;j = n;Ans = ""
    while i>0 and j>0:
        if A[i-1] == B[j-1]:
            Ans += A[i-1]
            i-=1;j-=1
        else:
            a = d[i][j-1] ; b =d[i-1][j]
            if a > b:
                j-=1
            else:
                i-=1
    return Ans[::-1]

A = input()
B = input()
print(longestsub(A,B))