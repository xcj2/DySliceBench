from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque


def read():
    return int(input())


def readmap():
    return map(int, input().split())


def readlist():
    return list(map(int, input().split()))


N, K = readmap()
A = readlist()
ind1 = A.index(1)

ans = 100000
for k in range(max(0, ind1 - K + 1), ind1 + 1):
    left = int(math.ceil(k / (K - 1)))
    right = max(0, int(math.ceil((N - k - K) / (K - 1))))
    ans = min(ans, left + right + 1)

print(ans)