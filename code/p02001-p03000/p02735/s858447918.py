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
dis = [[0 for i in range(w+1)]for j in range(h+1)] # 障害物に当たる最小数
for i in range(2,w+1):
    dis[0][i] = inf
for i in range(2,h+1):
    dis[i][0] = inf
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            dis[i+1][j+1] = min(dis[i][j+1], dis[i+1][j])
        else:
            if i>0 and j>0 and s[i-1][j]=='#' and s[i][j-1]=='#':
                dis[i+1][j+1] = min(dis[i][j+1], dis[i+1][j])
            elif i>0 and s[i-1][j]=='#':
                dis[i+1][j+1] = min(dis[i][j+1], dis[i+1][j]+1)
            elif j>0 and s[i][j-1]=='#':
                dis[i+1][j+1] = min(dis[i][j+1]+1, dis[i+1][j])
            else:
                dis[i+1][j+1] = min(dis[i][j+1]+1, dis[i+1][j]+1)
print(dis[h][w])