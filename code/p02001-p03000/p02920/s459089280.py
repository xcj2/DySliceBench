#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    n = II()
    print(n**3)
    return

#B
def B():
    n = II()
    a = LI()
    b = LI()
    c = LI()
    ans = 0
    for i in range(n):
        ans += b[a[i] - 1] + (c[a[i] - 1] if i != n - 1 and a[i] + 1 == a[i + 1] else 0)
    print(ans)
    return

#C
def C():
    n = II()
    b = LI()
    ans = b[0]
    for i in range(n-2):
        if b[i] >= b[i + 1]:
            ans += b[i + 1]
        else:
            ans += b[i]
    print(ans+b[-1])
    return

#D
def D():
    n, k = LI()
    s = S()
    a = []
    for i in range(n):
        if i == n - 1:
            a.append(s[i])
        elif s[i] != s[i + 1]:
            a.append(s[i])
    print(min(n - 1, n - len(a) + 2 * k))
    return

# E
# 解説AC
# Piが何個使えるかというとこまでは良くて
# そのPiよりも大きい数字が左に2個右に2個必要というところまではいけた
# 問題の本質を解決できてはいない
# ここから解説
# 大きい順からみて見たものに対してインデックスを保持
# ここからbisectを使えばlogNでi付近のすでに追加したインデックスを持ってこれる
# あと少しだけどその少しが遠い
# ↑
# これは嘘
# BITを使え
class BinaryIndexedTree:
    # http://hos.ac/slides/20140319_bit.pdf
    def __init__(self, size):
        """
        :param int size:
        """
        self.bit = [0 for _ in range(size)]
        self.size = size

    def add(self, i, w):
        """
        i番目にwを加える
        :param int i:
        :param int w:
        :return:
        """
        x = i
        while x < self.size:
            self.bit[x] += w
            x += x & -x
        return

    def sum(self, i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i
        while x > 0:
            res += self.bit[x]
            x -= x & -x
        return res

    def search(self, x):
        """
        二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        :param int x:
        :return :
        """
        ok = self.size
        ng = 0
        while abs(ok - ng) != 1:
            mid = (ok + ng)//2
            if self.sum(mid) >= x:
                ok = mid
            else:
                ng = mid
        return ok

    def __len__(self):
        return self.size

def E():
    n = II()
    a = LI()
    dic = defaultdict(int)
    for i, ai in enumerate(a):
        dic[ai] = i+1
    bit = BinaryIndexedTree(n+1)
    num = [i + 1 for i in range(n)][::-1]
    ans = 0
    for i in num:
        c = dic[i]
        L = bit.sum(c)
        bit.add(c,1)
        R = n-i-L 
        a = bit.search(L-1) if L >= 2 else 0
        b = bit.search(L) if L >= 1 else 0
        d = bit.search(L+2) if R >= 1 else n+1
        e = bit.search(L+3) if R >= 2 else n+1
        tmp = 0
        if b != 0:
            tmp += (b-a) * (d-c)
        if d != 0:
            tmp += (e-d) * (c-b)
        ans += i * tmp

    print(ans)
    return

#F
def F():
    def root(x):
        if x == par[x]:
            return x
        par[x] = root(par[x])
        return par[x]
    def unite(x, y):
        x = root(x)
        y = root(y)
        if x == y: return
        if x > y: y, x = x, y
        par[x] = y
        return
    n = II()
    s = LI()
    s.sort(reverse=True)
    x = list(sorted(set(s)))[::-1]
    d = defaultdict(int)
    di = defaultdict(int)
    for i, xi in enumerate(x):
        d[xi] = i
    ma = i + 1
    num = [0] * (ma)
    par = [i for i in range(ma)]
    for si in s:
        num[d[si]] += 1
    l = [0]
    num[0] -= 1
    for _ in range(n):
        tmp = l[::1]
        for li in l:
            if root(li) + 1 < ma and num[root(li) + 1]:
                num[root(li)+1] -= 1
                tmp.append(root(li)+1)
            else:
                i = 0
                x = root(li)
                while root(x + i) + 1 < ma and (not num[root(x + i) + 1]):
                    i += 1
                unite(li, x + i)
                if root(li)+1 >= ma:
                    print("No")
                    return
                tmp.append(root(li)+1)
                num[root(li)+1] -= 1
        l = tmp[::1]
    print("Yes")
    return

#Solve
if __name__ == '__main__':
    F()