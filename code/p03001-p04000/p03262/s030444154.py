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


N, X = LI()
X_list = LI()

#  N = 10**5
#  X = 10**9
#  X_list = [i for i in range(1, 10**5, 5)]

#  if N == 1:
#      print(abs(X_list[0] - 1))
#      exit()
X_list.sort()

bisect.insort_left(X_list, X)
#  print(X_list)
X_diff = [abs(j-i) for i, j in zip(X_list[:-1], X_list[1:])]
X_diff = list(set(X_diff))
#  result = min(X_diff)
# 全部行けない場合がある
# 1 4 9 など
# すべてステップ幅-1で割り切れなければ不可

def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)

for i in range(len(X_diff)):
    #  print(i)
    if i == 0:
        result = X_diff[i]
        continue
    
    result = gcd(X_diff[i], result)
#  while True:
#      if all(x % result == 0 for x in X_diff):
#          result = i
#      else:
#          result = [i for i in range(result, 0, -1) if ]

print(result)
