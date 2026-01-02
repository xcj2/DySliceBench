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
def S(): return input()
def pf(s): return print(s, flush=True)

N = I()
A = LI()

def f(num):
    return sum([num%a for a in A])
# 最大値の２倍-1まで順に探索していく
res = []
#  for i in range(max(A)*2+1):
#  for i in range(46*20*11*7):
#  for i in range(994*941*851):
res = 0
#  for i in range(10**7):
#  for i in range(min(A)-1, min(A)):
#  for i in range(max(A)-1, 10**10, max(A)):
#      # 他のすべての余りがa - 1になれば終了
#      for a in A:
#          if i % a != a - 1:
#              break
#      else:
#          print()
#      res = max(res, f(i))
#  print(res)
print(sum([a-1 for a in A]))
