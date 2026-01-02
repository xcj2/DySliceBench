
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

k,x=getints()

min_value = max(x - k + 1, -1000000)
max_value = min(x + k - 1,  1000000)

for i in range(min_value, max_value + 1):
    print(i, end=" ")
print("")