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

N, K = LI()
X = LI()
if 0 in X:
    X.remove(0)
    K -= 1

if K == 0:
    print(0)
    exit()
# 累積和を使う
distances = []
mid = bisect.bisect_left(X, 0)
#  print(mid)
#  if mid == 0:
#      # 正の数しかない
#      distances = [0]
#      for x in X:
#          distances.append(distances[-1] + x)
#      distances = distances[1:]
#  else:
#      # 負の数あり
#      negs = [0]
#      for x in X[:mid]:
#          # 負の数を足して逆にする
#          negs.append(negs[-1] + x)
#      negs = negs[::-1][:-1]
#      posi = [0]
#      for x in X[mid:]:
#          posi.append(posi[-1] + x)
#      posi = posi[1:]
#      distances = negs + posi

#  from itertools import accumulate
#  distances = list(accumulate(X))
for x in X:
    if x < 0:
        distances.append(-x)
    else:
        distances.append(x)
#  print('dist', distances)

#左端から右にずれていく。
results = []
for start in range(N):
    end = start + K
    if end > N: break
    #  print('start, end', start, end)
    #  if end >= len(X): break
    if start < mid < end:
        # 飛び越える場合
        results.append(min(distances[start], distances[end-1]) * 2 + max(distances[start], distances[end-1]))
    elif start >= mid:
        # 全部右側
        results.append(distances[end-1])
    else:
        results.append(distances[start])

#  print(results)
print(min(results))