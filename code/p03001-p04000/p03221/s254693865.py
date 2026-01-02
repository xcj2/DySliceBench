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

N, M = mi()
PYs = []
for i in range(M):
  p, y = mi()
  p -= 1 #0スタートに
  PYs.append((y, p, i)) #PY[2]は市の番号
PYs = sorted(PYs) #誕生した年で昇順ソート

PREFs = [0] * N #PREFs[0~N-1]で各県の市数にアクセス
#各PYsの要素を[属する県番号, 県に所属したときに振られた通し番号, ID]に書き換える
for i, (eachy, eachp, eachi) in enumerate(PYs):
  PREFs[eachp] += 1
  PYs[i] = [eachp+1, PREFs[eachp], eachi] #県番号を1スタートに戻す



#市の番号昇順でソートし直し
from operator import itemgetter
PYs = sorted(PYs, key=itemgetter(2)) #添字が変わっている
for p, num, i in PYs:
  print('{:06}{:06}'.format(p, num))


