import sys
sys.setrecursionlimit(1000000000)
import math
from math import gcd
def lcm(a, b): return a * b // gcd(a, b)
from itertools import count, permutations, combinations, chain, product
from functools import lru_cache
from collections import deque, defaultdict
from operator import itemgetter
from pprint import pprint
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
N1097 = 10**9 + 7

def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok

def get_inv(n, modp):
    return pow(n, modp-2, modp)

def factorials_list(n, modp):    # 10**6
    fs = [1]
    for i in range(1, n+1):
        fs.append(fs[-1] * i % modp)
    return fs

def invs_list(n, fs, modp):     # 10**6
    invs = [get_inv(fs[-1], modp)]
    for i in range(n, 1-1, -1):
        invs.append(invs[-1] * i % modp)
    invs.reverse()
    return invs

def comb(n, k, modp):
    num = 1
    for i in range(n, n-k, -1):
        num = num * i % modp
    den = 1
    for i in range(2, k+1):
        den = den * i % modp
    return num * get_inv(den, modp) % modp

def comb_from_list(n, k, modp, fs, invs):
    return fs[n] * invs[n-k] * invs[k] % modp

#

class UnionFindEx:
    def __init__(self, size):
        #正なら根の番号、負ならグループサイズ
        self.roots = [-1] * size
    def getRootID(self, i):
        r = self.roots[i]
        if r < 0:   #負なら根
            return i
        else:
            r = self.getRootID(r)
            self.roots[i] = r
            return r
    def getGroupSize(self, i):
        return -self.roots[self.getRootID(i)]
    def connect(self, i, j):
        r1, r2 = self.getRootID(i), self.getRootID(j)
        if r1 == r2:
            return False
        if self.getGroupSize(r1) < self.getGroupSize(r2):
            r1, r2 = r2, r1
        self.roots[r1] += self.roots[r2]    #サイズ更新
        self.roots[r2] = r1
        return True

Yes = 'Yes'
No = 'No'

from pprint import pprint

def main():
    N=ii()
    if N==1:
        print(0)
        return
    elif N==2:
        print(2)
        return
    ans = 0
    def get(n):
        l = [1]
        for _ in range(N):
            l.append(l[-1] * n % N1097)
        return l
    l8 = get(8)
    l9 = get(9)
    l10 = get(10)

    for i in range(N-1):
        fr = N - i - 1
        a = l8[i] * ((l10[fr] - l9[fr]) % N1097)
        a = (a*2) % N1097
        ans += a
        ans %= N1097
    print(ans)





main()

