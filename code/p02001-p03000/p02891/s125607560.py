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

s = input()
K = ir()
ind = len(s)-1
while ind > 0 and s[ind] == s[ind-1]:
    ind-=1
if ind == 0:
    print(len(s)*K//2)
else:
    tmp = ''.join([s[ind:], s[:ind]])
    k = 0
    ans_div = 0
    pre = ''
    for c in tmp:
        if c != pre:
            ans_div+=((k+1)//2)
            k=0
        else:
            k+=1
        pre = c
    ans_div +=((k+1)//2)
    fir = s[:ind]
    firc = 0
    las = s[ind:]
    lasc = 0
    k = 0
    pre = ''
    for c in fir:
        if c != pre:
            firc+=((k+1)//2)
            k=0
        else:
            k+=1
        pre = c
    firc += ((k+1)//2)
    k = 0
    pre = ''
    for c in las:
        if c != pre:
            lasc+=((k+1)//2)
            k=0
        else:
            k+=1
        pre = c
    lasc += ((k+1)//2)
    print(firc+lasc+ans_div*(K-1))