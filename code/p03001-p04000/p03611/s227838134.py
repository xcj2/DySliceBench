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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N = _I()
A = LI()

"""
最小値から最大値
の間には絶対収まる
1111155なら1でいい
なら、
各数字のカウントを保持する
"""
char_counts = [0]*(10**5+5)

for a in A:
    char_counts[a] += 1

#  print(char_counts[:10])

ans = 0
for i in range(min(A), max(A)+1):
    ans = max(ans, char_counts[i] + char_counts[i-1] + char_counts[i+1])
print(ans)
