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
nos = set(input().split())
#昇順ソート
availables = sorted(list(set(map(str, (0,1,2,3,4,5,6,7,8,9))) - nos))

#方針
#桁数が変われば、(1)0が使える場合は、使える一番低い数字+あとは全部0
#              (2)0が使えない場合は、使える一番低い数字で埋めるだけ
#とはいえ、元々が3桁とかなら全探索で十分
#5桁になると怪しいので、(1)(2)を活かす

#まずは9999までの間に答えがあるかどうか
#N=9999でも、9が嫌いじゃない場合があるから探索する
ans = 0
for i in range(N, 10000):
  if not (set(str(i)) & nos): #使えない(nos)のに使ってる(set内)が無かったら
    ans = i
    break
if ans == 0:
  #もしここまでで答えが出ていなかったら
  if '0' in availables:
    print(str(list(availables)[1])+str(list(availables)[0])*4)
    exit()
  else:
    print(str(list(availables)[0])*5)
    exit()

print(ans)

