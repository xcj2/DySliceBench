# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import fractions
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import Counter
from collections import deque
import pprint
import itertools

sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


# a^n
def power(a, n, mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod


# n*(n-1)*...*(l+1)*l
def kaijo(n, l, mod):
    if n == 0:
        return 1
    a = n
    tmp = n - 1
    while (tmp >= l):
        a = a * tmp % mod
        tmp -= 1
    return a


inf = 10 ** 18
mod = 10 ** 9 + 7

h,w = lr()
s = [input() for i in range(h)]
dicw = [[0 for j in range(w)] for i in range(h)]
dich = [[0 for j in range(w)] for i in range(h)]
# まずは横方向の情報を格納
for i in range(h):
    ind = 0
    now = 0
    while ind < w:
        now = 0
        while ind < w and s[i][ind] == '.':
            now+=1
            ind+=1
        for j in range(now):
            dicw[i][ind-1-j] = now
        ind+=1
for i in range(w):
    ind = 0
    now = 0
    while ind < h:
        now = 0
        while ind < h and s[ind][i] == '.':
            now+=1
            ind+=1
        for j in range(now):
            dich[ind-1-j][i] = now
        ind+=1

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            ans = max(ans, dich[i][j]+dicw[i][j]-1)
print(ans)
