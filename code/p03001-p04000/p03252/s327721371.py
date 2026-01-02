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

S = input()
T = input()

stlist = [[sc, tc] for sc, tc in zip(S, T)]


from operator import itemgetter

#まずはsでソート
stlist = sorted(stlist, key=itemgetter(0))

#同じ文字なのに違うことがあるか
prevsc = 'Z'
prevtc = 'Z' #これは無意味だが、とりあえず宣言しておく
for sc, tc in stlist:
  if prevsc == sc and prevtc != tc:
    print('No')
    exit()
  else:
    prevsc = sc
    prevtc = tc


#tでソート
stlist = sorted(stlist, key=itemgetter(1))

#同じ文字なのに違うことがあるか
prevsc = 'Z' #これは無意味だが、とりあえず宣言しておく
prevtc = 'Z'
for sc, tc in stlist:
  if prevtc == tc and prevsc != sc:
    print('No')
    exit()
  else:
    prevsc = sc
    prevtc = tc

print('Yes')

