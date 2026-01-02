import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)
from collections import deque


def getN():
    return int(input())


def getList():
    return list(map(int, input().split()))


import math

n = getN()

match = [0 for i in range((n * (n - 1)) // 2)]
child = [[] for i in range((n * (n - 1)) // 2)]
iriji = [0 for i in range((n * (n - 1)) // 2)]


def toposo(n, iriji, child):
    order = [0 for i in range((n*(n+1))//2)]
    q = deque([])
    for i, iri in enumerate(iriji):
        if iri == 0:
            q.append(i)
            order[i] = 1
    while(q):
        start = q.popleft()
        target = child[start]
        for tgt in target:
            iriji[tgt] -= 1
            if iriji[tgt] == 0:
                q.append(tgt)
                order[tgt] = order[start] + 1

    if sum(iriji) != 0:
        return -1

    else:
        return max(order)


for idd in range(n):
    nums = getList()
    i = idd + 1
    for j, k in zip(nums, nums[1:]):
        ii, j = min(i, j), max(i, j)
        iii, k = min(i, k), max(i, k)
        idx1 = ((j - 1) * (j - 2)) // 2 + (ii - 1)
        idx2 = ((k - 1) * (k - 2)) // 2 + (iii - 1)
        iriji[idx2] += 1
        child[idx1].append(idx2)
        # print(i, j, k)
        # print(idx1, idx2)

#
# print(child)
# print(isroot)
# # sys.exit()
#
# bfs()
# # print("gg")
# ans = 1
# for m in match:
#     if m > ans:
#         ans = m
#     if m == 0:
#         print(-1)
#         sys.exit()
# print(iriji, child)

print(toposo(n, iriji, child))