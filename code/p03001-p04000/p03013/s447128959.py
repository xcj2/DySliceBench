import math
import collections
import itertools
import sys
import bisect
from heapq import heappop,heappush
sys.setrecursionlimit(10**6)
def MAP(): return list(map(int,input().split()))
def INT(): return int(input())
def FLOAT(): return float(input())
MOD = 10**9+7

n,m = MAP()
a = [INT() for _ in range(m)]

# 高速版
def fib(n):
    if n <= 1:
        return n
    result = [1, 0, 0, 1]
    matrix = [1, 1, 1, 0]
    while n > 0:
        if n % 2:
            result = mul(matrix, result)
        matrix = mul(matrix, matrix)
        n //= 2
    return result[2]

def mul(a, b):
    return [a[0]*b[0] + a[1]*b[2],
            a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2],
            a[2]*b[1] + a[3]*b[3]]

start = 0
ans = 1

for k in a:
    tmp = k-start
    if tmp==0:
        print(0)
        exit(0)
    ans *= fib(tmp)
    ans%=MOD
    start = k+1

ans*=fib(n-start+1)
ans%=MOD

print(ans)