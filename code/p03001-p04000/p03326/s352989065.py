import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math

def delicious(nums, param, m):
    res = 0
    cand = []
    for num in nums:
        tmp = 0
        for nu, pa in zip(num, param):
            # print(((-1)**int(pa)))
            tmp += nu *((-1)**int(pa))
        cand.append(tmp)

    return sum(sorted(cand, reverse=True)[:m])


n, m = getList()

nums = []
for i in range(n):
    nums.append(getList())

ans = 0
for i in range(8):
    param = format(i, "b").zfill(3)
    tmp = delicious(nums, param, m)
    # print(i, param, tmp)
    if ans < tmp:
        ans = tmp

print(ans)