def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))

from collections import defaultdict, deque
from sys import exit
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
n, k = getList()
# dist
nums = [0] + getList()
cnt = 1
if k == 1:
    print(1)
    exit()
cur = 1
visited = [-1 for i in range(n + 1)]
visited[1] = 1
rooped = False
while True:
    # cur 行き先
    cur = nums[cur]
    cnt += 1

    # １回目に訪れていたら
    if visited[cur] != -1:
        # ループの周期
        roop = cnt - visited[cur]
        # 途中を飛ばす
        k -= ((k-cnt) // roop) * roop
        rooped = True
    if not rooped:
        # １回目に訪れたのであれば
        visited[cur] = cnt

    if cnt == k:
        print(nums[cur])
        break