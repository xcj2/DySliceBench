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

n,a,b,c = lr()
l = [ir() for i in range(n)]
l.sort(reverse=True)

def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)

ans = inf

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            now = [l[i],l[j],l[k]]
            ret = [0 for w in range(5-(n-3))]
            pre = 0
            for g in range(n):
                if g!=i and g!=j and g!=k:
                    ret.append(l[g])
            for h in range(4**(n-3)):
                now = [l[i], l[j], l[k]]
                pre = 0
                judge = base10to(h, 4)
                tmp = ''
                for w in range(5-len(judge)):
                    tmp = ''.join([tmp,'0'])
                judge = ''.join([tmp,judge])

                for p,t in enumerate(judge):
                    if t == '1':
                        now[0]+=ret[p]
                        pre+=10
                    elif t == '2':
                        now[1]+=ret[p]
                        pre+=10
                    elif t == '3':
                        now[2]+=ret[p]
                        pre+=10
                now.sort(reverse=True)
                ans = min(ans,pre+abs(a-now[0])+abs(b-now[1])+abs(c-now[2]))
print(ans)