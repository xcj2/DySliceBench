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
INF = 10 ** 17

def main():
    n, k = getList()
    nums = [0] + getList()
    cnt = 1
    if k == 1:
        print(1)
        return
    cur = 1
    visited = [-1 for i in range(n+1)]
    visited[1] = 1
    rooped = False
    while(True):
        cur = nums[cur]
        cnt += 1

        if visited[cur] != -1:
            roop = cnt - visited[cur]
            k -= ((k-cnt) // roop) * roop
            rooped = True
        if not rooped:
            visited[cur] = cnt


        if cnt == k:
            print(nums[cur])
            return

        # print(k, cnt, cur)
        # print(visited)
        # if cnt >= 10:
        #     break

if __name__ == "__main__":
    main()

