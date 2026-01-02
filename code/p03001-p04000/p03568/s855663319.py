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

oddans = 1
for a in As:
  if a % 2 == 1:
    #自身が奇数なら、自身を選ぶしかない
    continue
  else:
    #自身が偶数なら、両側の奇数を選ぶことができる
    oddans *= 2

print(pow(3, N) - oddans)








