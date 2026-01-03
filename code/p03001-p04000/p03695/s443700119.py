import math
import string
import collections
from collections import Counter
from collections import deque


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
N = int(input())
a = readints()


def minimum(l):
    c = 0
    for i in range(len(l)):
        if l[i] == 'choose':
            c += 1
    if len(l) == c:
        return 1
    while 'choose' in l:
        l.remove('choose')
        # print(l)
    x = list(set(l))
    return len(x)


color = []
for i in range(N):
    if 1 <= a[i] and a[i] <= 399:
        color.append('gray')
    elif 400 <= a[i] and a[i] <= 799:
        color.append('brown')
    elif 800 <= a[i] and a[i] <= 1199:
        color.append('green')
    elif 1200 <= a[i] and a[i] <= 1599:
        color.append('light blue')
    elif 1600 <= a[i] and a[i] <= 1999:
        color.append('blue')
    elif 2000 <= a[i] and a[i] <= 2399:
        color.append('yellow')
    elif 2400 <= a[i] and a[i] <= 2799:
        color.append('orange')
    elif 2800 <= a[i] and a[i] <= 3199:
        color.append('red')
    elif 3200 <= a[i]:
        color.append('choose')
cnt = color.count('choose')
while 'choose' in color:
    color.remove('choose')
print(minimum(color), len(set(color))+cnt)
