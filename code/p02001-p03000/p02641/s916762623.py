import math
import string
import collections
from collections import Counter
from collections import deque
from decimal import Decimal
import sys
import fractions
from operator import itemgetter


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
x, n = map(int, input().split())
if n == 0:
    print(x)
    exit()
p = readints()
tmp = list(range(-200, 201))
# print(tmp)
for i in range(n):
    tmp.remove(p[i])
#print('tmp', tmp)
ans = [None]*500

for i in range(len(tmp)):
    ans[tmp[i]] = abs(tmp[i]-x)
# print(ans)
x = 10**5
for i in range(len(ans)):
    if ans[i] != None:
        x = min(x, ans[i])
# print(x)
print(ans.index(x))
