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
import math
import copy
from bisect import bisect_left

import sys
# sys.setrecursionlimit(1000000)
# list(map(int, input().split()))
mod = 10 ** 9 + 7

N = getN()
A = getList()
lista = [[0, 0] for i in range(61)]
# bitの各桁が１か０かをlistaに収納
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            lista[i][1] += 1
        else:
            lista[i][0] += 1
for i in A:
    splitbit(i)
ans = 0
for i in range(61):
    ans += ((lista[i][0] * lista[i][1]) * (2 ** i)) % mod
print(ans % mod)