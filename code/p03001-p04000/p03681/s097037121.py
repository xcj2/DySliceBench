
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n,m=getints()

if abs(n-m) > 1:
    print(0)
    exit(0)

mod = 10**9 + 7
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
        res %= mod
    return res

res = 0
if n == m:
    res = factorial(n) * factorial(m) * 2 % mod
else:
    res = factorial(n) * factorial(m) % mod

print(res)
