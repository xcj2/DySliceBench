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
    dp = [0]*N
    for pos in range(N):
        if pos == 0:
            dp[pos] = 0
        elif pos == 1:
            dp[pos]  = abs(A[pos-1] - A[pos])
        else:
            dp[pos]= min(abs(A[pos] - A[pos-1]) + dp[pos-1], abs(A[pos] - A[pos-2]) + dp[pos-2])
    return dp[-1]

N = int(input())
A = alele()
print(fun(A,N))