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
c = [None]*3
for i in range(3):
    c[i] = [None]*3
for i in range(3):
    c[i] = readints()
# print(c)
# a1=0,a2=1,a3=0,b1=1,b2=0,b3=1
#a = [0, 1, 0]
#b = [1, 0, 1]


def func(a, b):
    for i in range(3):
        for j in range(3):
            if a[i]+b[j] == c[i][j]:
                continue
            return False
            break
    return True


a = [None]*3
b = [None]*3

for i in range(101):
    for j in range(101):
        for k in range(101):
            for l in range(3):
                a[0] = i
                a[1] = j
                a[2] = k
                b[0] = c[l][0]-a[l]
                b[1] = c[l][1]-a[l]
                b[2] = c[l][2]-a[l]
                if func(a, b):
                    print('Yes')
                    exit()
print('No')
