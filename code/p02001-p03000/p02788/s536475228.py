#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import bisect

n, d, a = [int(item) for item in input().split()]
places = []
xh = []
for i in range(n):
    x, h = [int(item) for item in input().split()]
    xh.append((x, h))
    places.append(x)
xh.sort()
places.sort()

N = 2**((n - 1).bit_length())
data0 = [0]*(N+1)
data1 = [0]*(N+1)
# 区間[l, r)に x を加算
def _add(data, k, x):
    while k <= N:
        data[k] += x
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1))
    _add(data0, r, x*(r-1))
    _add(data1, l, x)
    _add(data1, r, -x)

# 区間[l, r)の和を求める
def _get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s
def query(l, r):
    return _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)

ans = 0
for i, (x, h) in enumerate(xh):
    init_damage = (query(1, i+2) - query(1, i+1)) * a
    if init_damage >= h:
        continue
    bomb = (h - init_damage + a - 1) // a
    ans += bomb
    r_lim = bisect.bisect_right(places, x+2*d)
    add(1, r_lim+1, bomb)
print(ans)