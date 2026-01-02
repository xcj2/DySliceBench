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

n = int(input())
v = readints()
cnt = 0
tmp = [0]*(10**5+1)
tmp2 = [0]*(10**5+1)
for i in range(n):
    if i % 2 == 0:
        tmp[v[i]] += 1
    else:
        tmp2[v[i]] += 1
tmp_max = 0
tmp2_max = 0
for i in range(len(tmp)):
    if tmp[tmp_max] < tmp[i]:
        tmp_max = i
for i in range(len(tmp2)):
    if tmp2[tmp2_max] < tmp2[i]:
        tmp2_max = i
if tmp_max != tmp2_max:
    cnt += (n//2)-tmp[tmp_max]
    cnt += (n//2)-tmp2[tmp2_max]
    print(cnt)
    exit()
tmp_max2 = 0
tmp2_max2 = 0
cnt2 = 0
cnt3 = 0
for i in range(len(tmp)):
    if i != tmp_max:
        if tmp[tmp_max2] < tmp[i]:
            tmp_max2 = i
for i in range(len(tmp2)):
    if i != tmp2_max:
        if tmp2[tmp2_max2] < tmp2[i]:
            tmp2_max2 = i
cnt2 = (n//2)-tmp[tmp_max]+(n//2)-tmp2[tmp2_max2]
cnt3 = (n//2)-tmp2[tmp2_max]+(n//2)-tmp[tmp_max2]
print(min(cnt2, cnt3))
# print(tmp_max)
# print(tmp2_max)
# print(tmp_max2)
# print(tmp2_max2)
