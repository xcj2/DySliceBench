def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

from collections import defaultdict, deque
from sys import exit
import heapq
import math
import copy
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
# list(map(int, input().split()))
N, K = getNM()
intlist = [i for i in range(10)]
D = getList()
for i in D:
    if i in D:
        intlist.pop(intlist.index(i))

anslist = []
def dfs(i, num):
    anslist.append(num)
    if i < 5:
        for j in intlist:
            newnum = int(str(num) + str(j))
            dfs(i + 1, newnum)

for i in intlist:
    if i != 0:
        dfs(1, i)

anslist.sort()

for i in anslist:
    if i >= N:
        ans = i
        break
print(ans)