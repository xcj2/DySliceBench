import itertools
import math
import string
import collections
from collections import Counter
from collections import deque
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

n, m, q = map(int, input().split())
abcd = []
for i in range(q):
    abcd.append(readints())
# print(abcd)

tmp = []


def func(n, l):
    global tmp
    if len(l) == n:
        tmp.append(l)
        return
    if l == []:
        for i in range(1, m+1):
            func(n, []+[i])
        return
    for i in range(l[-1], m+1):
        func(n, l+[i])


func(n, [])
# print(tmp)


def func2(l):
    global abcd
    global q
    tmptmp = 0
    for i in range(q):
        # print(abcd[i])
        # print(q)
        # print(i)
        if l[abcd[i][1]-1]-l[abcd[i][0]-1] == abcd[i][2]:
            tmptmp += abcd[i][3]
    return tmptmp


tmp2 = []
for i in range(len(tmp)):
    tmp2.append(func2(tmp[i]))
# print(tmp2)
maxx = -100
for i in range(len(tmp2)):
    maxx = max(maxx, tmp2[i])

print(maxx)
