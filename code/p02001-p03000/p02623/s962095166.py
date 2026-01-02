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

n,m,k = lr()
a = lr()
b = lr()
a1 = [0]
b1 = [0]
for num in a:
    a1.append(a1[-1]+num)
for num in b:
    b1.append(b1[-1]+num)
def sumAreaA(l,r):
    return a1[r]-a1[l]
def sumAreaB(l,r):
    return b1[r]-b1[l]

ans = 0
dame = bisect.bisect_left(a1,k)
if dame < n+1:
    if a1[dame] == k:
        dame+=1
for i in range(dame):
    pre = i
    pretime = sumAreaA(0,i)
    time = k-pretime
    ind = bisect.bisect_left(b1,time)
    if ind == 0:
        ans = max(ans,pre)
    elif ind < m+1:
        if b1[ind] != time:
            ind-=1
        ans = max(ans,pre+ind)
    else:
        ans = max(ans, pre+m)
print(ans)