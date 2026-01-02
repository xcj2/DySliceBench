
import bisect
import collections
import itertools

def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

n=getint()
s=input()

west_count = [0]*n
west_count[0] = 1 if s[0] == 'W' else 0
for i in range(1, n):
    west_count[i] = west_count[i - 1] + (1 if s[i] == 'W' else 0)

east_count = [0]*n
east_count[-1] = 1 if s[-1] == 'E' else 0
for i in range(n-2,-1,-1):
    east_count[i] = east_count[i + 1] + (1 if s[i] == 'E' else 0)

res = n
for i in range(n):
    tmp = west_count[i - 1] if i > 0 else 0
    tmp += east_count[i + 1] if i < n - 1 else 0
    res = min(res, tmp)

print(res)
