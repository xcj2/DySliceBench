import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
ilele = lambda: map(int,input().split())
alele = lambda: list(map(int, input().split()))
ilelec = lambda: map(int1,input().split())
alelec = lambda: list(map(int1, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])

def findProductSum(A, n): 
    T = list(accumulate(A[::-1]))[::-1]
    #print(T)
    Ans = 0
    for i in range(n-1):
        x = A[i]*T[i+1]
        x %= MOD
        Ans += x
        Ans%= MOD
    return Ans
    

N= int(input())
A  = alele()
print(int(findProductSum(A,N) % MOD))
        