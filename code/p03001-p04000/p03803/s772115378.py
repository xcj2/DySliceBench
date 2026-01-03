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
ab = readints()
if ab[0] == 1 and ab[1] == 1:
    print('Draw')
    exit()
if ab[0] == 1:
    print('Alice')
    exit()
if ab[1] == 1:
    print('Bob')
    exit()
if ab[0] < ab[1]:
    print('Bob')
    exit()
if ab[0] > ab[1]:
    print('Alice')
    exit()
if ab[0] == ab[1]:
    print('Draw')
#t = list(map(str, input()))
# print(t)
#p_cnt = 0
#d_cnt = 0
# for i in range(len(t)):
#    if t[i] == 'P':
#        p_cnt += 1
#    if t[i] == 'D':
#        d_cnt += 1
# if p_cnt > d_cnt:
#    for i in range(len(t)):
#        if t[i] == '?':
#            if t[i-1] == 'P':
#                t[i] = 'D'
#            if t[i-1] == 'D':
#                t[i] = 'P'
#    tt = ''.join(t)
#    print(tt)
# else:
#    for i in range(len(t)):
#        if t[i] == '?':
#            t[i] = 'D'
#    tt = ''.join(t)
#    print(tt)
#
