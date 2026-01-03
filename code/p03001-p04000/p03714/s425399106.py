###template###
import sys
def input(): return sys.stdin.readline().rstrip()
from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt, ceil, floor
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
import heapq
INF = float("inf")
sys.setrecursionlimit(10**7)
# 4近傍（右, 下, 左, 上）
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
def inside(y: int, x: int, H: int, W: int) -> bool: return 0 <= y < H and 0 <= x < W
def mi(): return map(int, input().split())
def ii(): return int(input())
###template###

N = ii()
As = list(mi())
minusAs = [-a for a in As]

#下準備。左側0～N-1, 右側2N～3N-1のN要素のheapqを作っておく
#leftQは大きいのを残したい（最小値を取り除く）、rightQは小さいのを残したい（最大値を取り除く）ので、leftQはそのままの配列、rightQは符号反転したminusAsを使用する
leftQ = As[:N]
rightQ = minusAs[-N:]
heapq.heapify(leftQ)
heapq.heapify(rightQ)

#この配列のidxは、右端（左端）から何番目(0スタート)の区切りを採用するかを表す。あとで突き合わせる時に添字でバグらせないよう注意
leftsum = [0]*(N+1)
rightsum = [0]*(N+1) #どうせ最後に引くんだから、マイナスのまま入れちゃう
#つまり、最後に最小値を求める時は、逆に「最も大きい＝マイナス幅が小さいsum」を求めることになるので注意

#初期値はもう入れておく
leftsum[0] = sum(leftQ)
rightsum[0] = sum(rightQ)

for i in range(N, 2*N): #左端（右端）から最低N個（N-1まで）は済んでいる。残りはNまで～2N-1まで)
  #iがNのとき、左側は[:N], 右側は[-N:]
  #iが2Nのとき、左側は[0:2N], 右側は[-2N:]
  if leftQ[0] < As[i]: #大きいのを残したいので、最小値のが小さければ入れ替える
    #入れ替える
    nowmin = heapq.heappop(leftQ)
    leftsum[i-N+1] = leftsum[i-N] - nowmin + As[i]
    heapq.heappush(leftQ,As[i])
  else: leftsum[i-N+1] = leftsum[i-N] #そうでなければ入れ替えない
  if rightQ[0] < minusAs[-1-i]: #小さいのを残したいので、マイナス幅が大きければ入れ替える
    nowmax = heapq.heappop(rightQ)
    rightsum[i-N+1] = rightsum[i-N] - nowmax + minusAs[-1-i]
    heapq.heappush(rightQ,minusAs[-1-i])
  else: rightsum[i-N+1] = rightsum[i-N] #そうでなければ入れ替えない

ans = -INF
for lsum, rsum in zip(leftsum, rightsum[::-1]):
#  print(ans, lsum, rsum)
  ans = max(ans, lsum+rsum)

print(ans)
