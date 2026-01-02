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
nums = [0 for _ in range(5)]
ans = 0

for _ in range(N):
  s = input()
  if s[0] == 'M':
    nums[0] += 1
  elif s[0] == 'A':
    nums[1] += 1
  elif s[0] == 'R':
    nums[2] += 1
  elif s[0] == 'C':
    nums[3] += 1
  elif s[0] == 'H':
    nums[4] += 1

for i, j, k in combinations(range(5), 3):
  ans += nums[i] * nums[j] * nums[k]

print(ans)


