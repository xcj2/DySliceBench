import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def pf(s): return print(s, flush=True)

H, W = LI()

rows = [['.' for i in range(W+2)]]
for i in range(H):
    row = input()
    chars = ['.']
    for w in range(W):
        chars.append(row[w])
    chars.append('.')
    rows.append(chars)
rows.append(['.' for i in range(W+2)])
#  for row in rows:
#      print(row)

# rows[高さ][幅]ができあがった
for h in range(1, H+1):
    for w in range(1, W+1):
        if rows[h][w] == '#':
            if not (rows[h][w-1] == '#' or rows[h][w+1] == '#' or rows[h-1][w] == '#' or rows[h+1][w] == '#'):
                print('No')
                exit()
print('Yes')
