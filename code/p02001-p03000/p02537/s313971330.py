import math
import sys
import os

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")

###
class SegmentTree:
    """
    セグメント木: 区間の最大値等を効率よく更新する
    1.update: i番目の値をxに更新する
    2.query: 区間[l, r)の値を得る
    """
 
    def __init__(self, n, func, intv, A=[]):
        """
        :param n: 要素数(0-indexed)
        :param func: 値の操作に使う関数(min, max, add, gcdなど)
        :param intv: 要素の初期値(単位元)
        :param A: 初期化に使うリスト(オプション)
        """
        self.n = n
        self.func = func
        self.intv = intv
        # nより大きい2の冪数
        n2 = 1
        while n2 < n:
            n2 <<= 1
        self.n2 = n2
        self.tree = [self.intv] * (n2 << 1)
        # 初期化の値が決まっている場合
        if A:
            # 1段目(最下段)の初期化
            for i in range(n):
                self.tree[n2+i] = A[i]
            # 2段目以降の初期化
            for i in range(n2-1, -1, -1):
                self.tree[i] = self.func(self.tree[i*2], self.tree[i*2+1])
 
    def update(self, i, x):
        """
        i番目の値をxに更新
        :param i: index(0-indexed)
        :param x: update value
        """
        i += self.n2
        self.tree[i] = x
        while i > 0:
            i >>= 1
            self.tree[i] = self.func(self.tree[i*2], self.tree[i*2+1])
 
    def add(self, i, x):
        self.update(i, self.get(i) + x)
 
    def query(self, a, b):
        """
        [a, b)の値を得る
        :param a: index(0-indexed)
        :param b: index(0-indexed)
        """
        l = a + self.n2
        r = b + self.n2
        s = self.intv
        while l < r:
            if r & 1:
                r -= 1
                s = self.func(s, self.tree[r])
            if l & 1:
                s = self.func(s, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return s
 
    def get(self, i):
        """ 一点取得 """
        return self.tree[i+self.n2]
 
    def all(self):
        """ 全区間[0, n)の取得 """
        return self.tree[1]
 
    def bisearch_fore(self, l, r, x, func):
        """ 区間[l,r]で左から最初にxに対して比較の条件を満たすような値が出現する位置 """
 
        ok = r + 1
        ng = l - 1
        while ng+1 < ok:
            mid = (ok+ng) // 2
            if func(self.query(l, mid+1), x):
                ok = mid
            else:
                ng = mid
        if ok != r + 1:
            return ok
        else:
            return INF
 
    def bisearch_back(self, l, r, x, func):
        """ 区間[l,r]で右から最初にxに対して比較の条件を満たすような値が出現する位置 """
 
        ok = l - 1
        ng = r + 1
        while ok+1 < ng:
            mid = (ok+ng) // 2
            if func(self.query(mid, r+1), x):
                ok = mid
            else:
                ng = mid
        if ok != l - 1:
            return ok
        else:
            return -INF
 
    def print(self):
        for i in range(self.n):
            print(self.get(i), end=' ')
        print()
###


N,K = LI()
A = [I() for _ in range(N)]
ans = 0

M = max(A)
seg = SegmentTree(M+1, max, -INF, [0]*(M+1))
 
for a in A:
    start = max(0, a - K)
    end = min(M, a + K) + 1
    res = seg.query(start, min(a+K, M)+1)
    # 区間の最大値をインクリメント
    res += 1
    seg.update(a, res)
ans = seg.all()
print(ans)


# t = [0]*300001

# for a in A:
#     start = max(0, a - K)
#     end = min(N + 1, a + K+1)
#     t[a]=max(t[start:end])+1

# ans = max(t)

# # ビット全探索
# for i in range(1 << N):
#     c = 0
#     flag = True
#     before = -1
#     for j in range(N):
#         if (i >> j) & 1 == 0:
#             continue
#         if not (before == -1) and abs(before - A[j])>K:
#             flag = False
#             break
#         before = A[j]
#         c += 1
#     # 全てX以上であれば更新
#     if flag:
#         ans = max(ans, c)

