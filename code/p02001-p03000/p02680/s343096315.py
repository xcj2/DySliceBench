from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint



sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007

n, m = LI()
horizontal = []
vertical = []
x_co = {INF, -INF}
y_co = {INF, -INF}
for _ in range(n):
    a, b, c = LI()
    x_co.add(a)
    x_co.add(b)
    y_co.add(c)
    vertical += [(a, b, c)]

for _ in range(m):
    d, e, f = LI()
    x_co.add(d)
    y_co.add(e)
    y_co.add(f)
    horizontal += [(d, e, f)]

x_len = len(x_co) * 2 - 1
y_len = len(y_co) * 2 - 1
x_co = sorted(list(x_co))
y_co = sorted(list(y_co))
x_comp = {val:i for i, val in enumerate(x_co)}
y_comp = {val:i for i, val in enumerate(y_co)}
grid = [[0] * y_len for _ in range(x_len)]

x_range = [0] * x_len
y_range = [0] * y_len
x_range[0] = x_range[-1] = INF
y_range[0] = y_range[-1] = INF

for i, (x1, x2) in enumerate(zip(x_co, x_co[1:])):
    x_range[i * 2 + 1] = x2 - x1
    if x1 <= 0 <= x2:
        sx = i * 2 + 1

for i, (y1, y2) in enumerate(zip(y_co, y_co[1:])):
    y_range[i * 2 + 1] = y2 - y1
    if y1 <= 0 <= y2:
        sy = i * 2 + 1


for a, b, c in vertical:
    y = y_comp[c] * 2
    for x in range(x_comp[a] * 2 + 1, x_comp[b] * 2 + 1, 2):
        grid[x][y] = 1

for d, e, f in horizontal:
    x = x_comp[d] * 2
    for y in range(y_comp[e] * 2 + 1, y_comp[f] * 2 + 1, 2):
        grid[x][y] = 1

ans = 0
dq = deque([(sx, sy)])
grid[sx][sy] = 1
diff = ((0, 1), (1, 0), (-1, 0), (0, -1))
ans += x_range[sx] * y_range[sy]
while dq:
    x, y = dq.popleft()
    for dx, dy in diff:
        nx, ny = dx + x, dy + y
        if grid[nx][ny]:
            continue
        nx += dx;
        ny += dy
        if grid[nx][ny]:
            continue
        grid[nx][ny] = 1
        dq.append((nx, ny))
        ans += x_range[nx] * y_range[ny]
        if ans >= INF:
            print("INF")
            exit()

print(ans)