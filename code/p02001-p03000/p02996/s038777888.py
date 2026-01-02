import itertools
import math
import string
import collections
from collections import Counter
from collections import deque
from operator import itemgetter
import sys
sys.setrecursionlimit(2*10**5)
INF = 2**60


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
n = int(input())
ab = [readints() for _ in range(n)]
# print(ab)
ab2 = sorted(ab, key=lambda x: x[1])
# print(ab2)
tmp = 0
cnt = 0
for i in range(n):

    tmp += ab2[i][0]
    if tmp <= ab2[i][1]:
        cnt += 1
if cnt == n:
    print('Yes')
    exit()
print('No')
