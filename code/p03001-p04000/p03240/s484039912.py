from copy import deepcopy
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
import copy


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


def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a


# coordinates
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
n = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(n)]
# print(xyh)


def get_H(Cx, Cy):
    for x, y, h in xyh:
        if h == 0:  # 高度が0のときは何もしない
            continue
        H = abs(x-Cx)+abs(y-Cy)+h  # H-|X-Cx|-|Y-Cy|=hの式変形
        if h >= 1:
            return H


def check(Cx, Cy, H):
    for x, y, h in xyh:
        if h != max(H-abs(x-Cx)-abs(y-Cy), 0):
            return False
    return True


for Cx in range(101):
    for Cy in range(101):
        H = get_H(Cx, Cy)
        if (check(Cx, Cy, H)):
            print(Cx, Cy, H)
            quit()
