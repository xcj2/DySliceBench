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
DEBUG = 'ONLINE_JUDGE' not in sys.argv

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

def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def main():
    H,W=mis()
    ch,cw=mis()
    ch-=1
    cw-=1
    dh,dw=mis()
    dh-=1
    dw-=1
    S = [input() for _ in range(H)]
    #
    q = deque()
    nq = deque()
    q.append((ch, cw))
    reached = set()
    reached.add((ch, cw))
    zone = set()
    m = 0
    #
    def isv(h, w):
        return (h, w) not in reached and 0<=h<H and 0<=w<W and S[h][w]=='.'
    #
    while True:
        while q:
            h, w = q.popleft()
            zone.add((h, w))
            for nh, nw in ((h+1, w), (h-1, w), (h, w+1), (h, w-1)):
                if isv(nh, nw):
                    q.append((nh, nw))
                    reached.add((nh, nw))
        if (dh, dw) in reached:
            print(m)
            return
        for h, w in zone:
            for th in range(-2+h, 2+1+h):
                for tw in range(-2+w, 2+1+w):
                    if isv(th, tw):
                        nq.append((th, tw))
                        reached.add((th, tw))
        m += 1
        zone.clear()
        q, nq = nq, q
        if not q:
            print(-1)
            return







main()

