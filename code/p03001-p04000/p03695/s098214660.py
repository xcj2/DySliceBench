import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal


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
a = readints()
ans = []
for i in range(n):
    if 1 <= a[i] and a[i] <= 399:
        ans.append('hai')
    if 400 <= a[i] and a[i] <= 799:
        ans.append('tya')
    if 800 <= a[i] and a[i] <= 1199:
        ans.append('midori')
    if 1200 <= a[i] and a[i] <= 1599:
        ans.append('mizu')
    if 1600 <= a[i] and a[i] <= 1999:
        ans.append('ao')
    if 2000 <= a[i] and a[i] <= 2399:
        ans.append('ki')
    if 2400 <= a[i] and a[i] <= 2799:
        ans.append('daidai')
    if 2800 <= a[i] and a[i] <= 3199:
        ans.append('aka')
    if a[i] >= 3200:
        ans.append('nanndemoii')
tmp = 0
for i in range(n):
    if ans[i] == 'nanndemoii':
        tmp += 1
if tmp == n:
    print(1, n)
    exit()
# print(ans)
set_ans = list(set(ans))
# print(set_ans)
min_cnt = 0
for i in range(len(set_ans)):
    if set_ans[i] != 'nanndemoii':
        min_cnt += 1
# print(min_cnt)
max_cnt = 0
for i in range(n):
    if ans[i] == 'nanndemoii':
        max_cnt += 1
max_cnt += min_cnt
print(min_cnt, max_cnt)
