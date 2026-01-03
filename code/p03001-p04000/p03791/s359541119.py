import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# 最速で何番目にゴールできるかを考える
# 自分より左のロボットを1,3,5,…に配置したい
# それが不可能なロボットの個数をカウントしていけば良い

N = I()
x = LI()

remove = [False]*N
place = 1
for i in range(N):
    if x[i] < place:
        remove[i] = True
    else:
        place += 2

first_goal = [1]*N
for i in range(1,N):
    if remove[i-1]:
        first_goal[i] = first_goal[i-1]+1
    else:
        first_goal[i] = first_goal[i-1]

d = defaultdict(int)
for i in range(N):
    d[first_goal[i]] += 1

dc = [0]*(N+1)
for i in range(1,N+1):
    dc[i] = dc[i-1]+d[i]

ans = 1
for i in range(1,N+1):
    ans *= dc[i]-(i-1)
    ans %= mod

print(ans)