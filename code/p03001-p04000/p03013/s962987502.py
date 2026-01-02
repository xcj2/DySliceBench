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

#  f = open('C_input_29.txt')
#  lines = f.readlines()
#  f.close()
#  N, M = map(int, lines[0].split())
#  A = []
#  for line in lines[1:]:
#      A.append(int(line))

N, M = LI()
A = set([_I() for i in range(M)])

#  if M != 0:
#      # 連続した壊れた段がある場合は0
#      B = [i for i in A]
#      B.remove(B[0])
#      B.append(10**15+100)
#      diffs = [b - a for a, b in zip(A,B)]
#      #  print(diffs)

#      if any(i == 1 for i in diffs):
#          # 隣同士なので0
#          print(0)
#          exit()
#  print('hoge')
"""
考え方
xにたどり着く通りは、x-1とx-2段目にたどり着く通りの合計
dp
3が障害のとき
1へは1通り
2へは0からと1からの2通り
3へは0通り
4へは2からの2通りと、3からの0通りで2通り
5へは3からの0通りと4からの2通りで2通り
6へは4からの2通りと5からの2通りで4通り
"""
#  dp = {}
dp = [0 for i in range(N+1)]
#  print('fua')
dp[0] = 1
dp[1] = 1 if 1 not in A else 0
#  [dp.update({i: (dp[i-1] + dp[i-2])%mod}) if i not in A else dp.update({i: 0}) for i in range(2, N+1)]
for i in range(2, N+1):
    #  print(i)
    # i段目までの通りを計算する
    if i not in A:
        # i段目が障害のときは0になっているので飛ばす
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= mod

print(dp[N])
