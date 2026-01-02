def main():
    examD()

def examA():
    K = I()
    ans = "ACL"*K
    print(ans)
    return

def examB():
    A, B, C, D = LI()
    if (A<=D and C<=A) or A<=C<=B:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
    return

def examC():
    class UnionFind():
        def __init__(self, n):
            self.parent = [-1 for _ in range(n)]
            # 正==子: 根の頂点番号 / 負==根: 連結頂点数

        def reset(self):
            self.parent = [-1] * len(self.parent)

        def find(self, x):
            # 要素xが属するグループの根を返す
            if self.parent[x] < 0:
                return x
            else:
                self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        def unite(self, x, y):
            # 要素xが属するグループと要素yが属するグループとを併合する
            x, y = self.find(x), self.find(y)
            if x == y:
                return False
            else:
                if self.size(x) < self.size(y):
                    x, y = y, x
                self.parent[x] += self.parent[y]
                self.parent[y] = x

        def same(self, x, y):
            # 要素x, yが同じグループに属するかどうかを返す
            return self.find(x) == self.find(y)

        def size(self, x):
            # 要素xが属するグループのサイズ（要素数）を返す
            x = self.find(x)
            return -self.parent[x]

        def is_root(self, x):
            # 要素の根をリストで返す
            return self.parent[x] < 0

        def roots(self):
            # すべての根の要素をリストで返す
            return [i for i, x in enumerate(self.parent) if x < 0]

        def members(self, x):
            # 要素xが属するグループに属する要素をリストで返す
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def group_count(self):
            # グループの数を返す
            return len(self.roots())

        def all_group_members(self):
            # {ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す
            return {r: self.members(r) for r in self.roots()}
    N, M = LI()
    uf = UnionFind(N)
    for _ in range(M):
        a, b = LI()
        a -= 1
        b -= 1
        uf.unite(a,b)

    ans = uf.group_count()-1
    print(ans)
    return

def examD():
    class segment_():
        def __init__(self, A, n, segfunc, ide_ele=0):
            #####単位元######要設定0or1orinf
            self.ide_ele = ide_ele
            ####################
            self.num = 1 << (n - 1).bit_length()
            self.seg = [self.ide_ele] * 2 * self.num
            self.segfunc = segfunc
            # set_val
            for i in range(n):
                self.seg[i + self.num] = A[i]
                # built
            for i in range(self.num - 1, 0, -1):
                self.seg[i] = self.segfunc(self.seg[2 * i], self.seg[2 * i + 1])

        def update(self, k, r):
            k += self.num
            self.seg[k] = r
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        # 値xに1加算
        def add(self, k, x=1):
            k += self.num
            self.seg[k] += x
            while k:
                k >>= 1
                self.seg[k] = self.segfunc(self.seg[k * 2], self.seg[k * 2 + 1])

        def query(self, p, q):
            # qは含まない
            if q < p:
                return self.ide_ele
            p += self.num;
            q += self.num
            res = self.ide_ele
            while p < q:
                if p & 1 == 1:
                    res = self.segfunc(res, self.seg[p])
                    p += 1
                if q & 1 == 1:
                    q -= 1
                    res = self.segfunc(res, self.seg[q])
                p >>= 1;
                q >>= 1
            return res
    N, K = LI()
    A = [I()for _ in range(N)]
    num = 3 * 10 ** 5 + 10
    Seg_max = segment_([0] * num, num, lambda a, b: max(a,b))
    dp = [0]*N
    dp[0] = 1
    Seg_max.update(A[0], dp[0])
    for i in range(1,N):
        a = A[i]
        l = max(0,a-K)
        r = min(num-1,a+K)
        cur = Seg_max.query(l,r+1)
        dp[i] = cur + 1
        Seg_max.update(a,dp[i])

    ans = max(dp)
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

def test():
    i = I()
    li = LI()
    lsi = LSI()
    si = LS()
    print(i)
    print(li)
    print(lsi)
    print(si)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,alphabet_convert,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 1<<31
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    main()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""