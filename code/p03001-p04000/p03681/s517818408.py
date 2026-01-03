from sys import stderr, setrecursionlimit, exit
from math import factorial
setrecursionlimit(2147483647)
def getInt():
    return int(input())
def getInts():
    return [int(i) for i in input().split()]
def getIntLines(n=1):
    res = []
    for _ in range(n):
        res.append(getInt())
    return res
def getIntsLines(n=1):
    res = []
    for _ in range(n):
        res.append(getInts())
    return res
def debug(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

mod = 10**9 + 7

n, m = getInts()
if abs(n-m) >= 2:
    print(0)
    exit()
else:
    a = factorial(min(n, m))
    if n == m:
        print((((a**2) % mod) * 2 ) % mod)
    else:
        print((((a**2) % mod) * max(m, n)) % mod)