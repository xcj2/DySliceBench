import math
import string
import collections
from collections import Counter


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
n, k = map(int, input().split())
h = readints()
h_sort = sorted(h, reverse=True)
# print(h_sort)
# print(h_sort[k:])
h_sort2 = h_sort[k:]
if h_sort2 == []:
    print(0)
    exit()
ans = 0
for i in range(len(h_sort2)):
    ans += h_sort2[i]
print(ans)
