
import bisect
import collections
import itertools


def getint(): return int(input())
def getints(): return list(map(int, input().split()))
def getint2d(rows): return [getints() for _ in range(rows)]
def getgrid(rows): return [input() for _ in range(rows)]
def array1d(n, value): return [value for _ in range(n)]
def array2d(n, m, value): return [array1d(m, value) for _ in range(n)]

def to_int():
    s = sorted(input())
    res = 0
    for c in s:
        c = ord(c)
        res = (res * 1337 + c) % 10**19+7
    return res

n=getint()
values = [to_int() for _ in range(n)]

cnt = collections.Counter()

for v in values:
    cnt[v] += 1

res = 0
for m in cnt.values():
    res += m * (m - 1) // 2

print(res)