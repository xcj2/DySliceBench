import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal
import sys
import fractions
from operator import itemgetter
import itertools


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
# print(a)
tmp = []
for i in range(n):
    if 1 <= a[i] and a[i] <= 399:
        tmp.append('ha')
    if 400 <= a[i] and a[i] <= 799:
        tmp.append('cha')
    if 800 <= a[i] and a[i] <= 1199:
        tmp.append('mi')
    if 1200 <= a[i] and a[i] <= 1599:
        tmp.append('mizu')
    if 1600 <= a[i] and a[i] <= 1999:
        tmp.append('ao')
    if 2000 <= a[i] and a[i] <= 2399:
        tmp.append('ki')
    if 2400 <= a[i] and a[i] <= 2799:
        tmp.append('da')
    if 2800 <= a[i] and a[i] <= 3199:
        tmp.append('aka')
    if 3200 <= a[i]:
        tmp.append('nanndemo')
# print(tmp)
z = 0
for i in range(len(tmp)):
    if tmp[i] == 'nanndemo':
        z += 1
if z == len(tmp):
    print(1, len(tmp))
    exit()

cnt = 0
tmp2 = list(set(tmp))
for i in range(len(tmp2)):
    if tmp2[i] != 'nanndemo':
        cnt += 1
min_x = cnt
#print('min', min_x)
cnt2 = 0
for i in range(len(tmp)):
    if tmp[i] == 'nanndemo':
        cnt2 += 1
# print(cnt2)
if cnt2 == 0:
    max_x = len(set(tmp))
    print(min_x, max_x)
    exit()
cnt3 = 0
if cnt2 != 0:
    for i in range(len(tmp2)):
        if tmp2[i] != 'nanndemo':
            cnt3 += 1
max_xx = cnt3+cnt2
print(min_x, max_xx)
