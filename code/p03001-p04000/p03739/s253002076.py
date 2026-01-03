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


# segment tree

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x, y: x + y, default=0):
        self.size = 2 ** (size - 1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default] * (self.size * 2)  # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i * 2], self.dat[i * 2 + 1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)  # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res


n = ir()
a = lr()
seg1 = SegmentTree(n, lambda x, y: x + y, 0)
seg2 = SegmentTree(n, lambda x, y: x + y, 0)
for i, num in enumerate(a):
    seg1.update(i, num)  # 0オリジンのi個目をnumに更新 O(n)
    seg2.update(i, num)  # 0オリジンのi個目をnumに更新 O(n)
ans1 = 0
ans2 = 0
pflag = True
pflag2 = False
for i in range(1,n+1):
    now1 = seg1.query(0,i)
    if pflag and now1 <= 0:
        seg1.update(i-1, a[i-1]-now1+1)
        ans1+=(1-now1)
    elif (not pflag) and now1 >= 0:
        seg1.update(i-1, a[i-1]-now1-1)
        ans1+=(now1+1)
    now2 = seg2.query(0,i)
    if pflag2 and now2 <= 0:
        seg2.update(i-1, a[i-1]-now2+1)
        ans2+=(1-now2)
    elif (not pflag2) and now2 >= 0:
        seg2.update(i-1, a[i-1]-now2-1)
        ans2+=(now2+1)
    pflag = not pflag
    pflag2 = not pflag2
print(min(ans1,ans2))
