#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
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
    n, i = LI()
    print(n-i+1)
    return

#B
def B():
    h, w = LI()
    a = SR(h)
    dy = defaultdict(int)
    dx = defaultdict(int)
    for y in range(h):
        for x in range(w):
            if a[y][x] == "#":
                dx[x] = 1
                dy[y] = 1
    dy = list(sorted(dy.items(), key=lambda x: x[0]))
    dx = list(sorted(dx.items(), key=lambda x: x[0]))
    for y,_ in dy:
        for x,_ in dx:
            print(a[y][x], end="")
        print()
    return

#C
def C():
    n, k = LI()
    x = LI()
    ans = inf
    for i in range(n - k + 1):
        if x[i] * x[i + k - 1] > 0:
            ans = min(ans, max(abs(x[i]), abs(x[i + k - 1])))
            continue
        ans = min(ans, min(abs(x[i]), abs(x[i + k - 1])) * 2 + max(abs(x[i]), abs(x[i + k - 1])))
    print(ans)
    return

# D
# 解説AC
def D():
    class BinaBinaryIndexedTree:
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
            x = i + 1
            while x <= self.size:
                self.bit[x - 1] += w
                x += x & -x
            return

        def sum(self, i):
            """
            [0,i]の合計
            :param int i:
            :return:
            """
            res = 0
            x = i + 1
            while x > 0:
                res += self.bit[x - 1]
                x -= x & -x
            return res

        def __len__(self):
            return self.size 

    def count_inversions(array, Max=None):
        """
        リストから転倒数 (array[i] > array[j] (i < j) となる (i, j) の組み合わせ数) を返す
        バブルソートするときに反転する必要がある数。
        :param list of int array:
                すべての要素が 0 以上の int である配列。
        :param int max: array の最大値。指定はわかる場合
        :rtype: int
        """
        if not Max:
            Max = max(array) + n
        bit = BinaBinaryIndexedTree(Max + 1)
        res = 0
        for i in range(len(array)):
            res += i - bit.sum(array[i])
            bit.add(array[i], 1)
        return res

    def f(i):
        x = a_sorted[i]
        c = [n] + [1 if e >= x else - 1 for e in a]
        for i in range(n):
            c[i + 1] += c[i]
        tmp = count_inversions(c, 2 * n)
        if invmax - tmp >= (invmax + 1) // 2:
            return True
        else:
            return False
        
        
        
    
    n = II()
    a = LI()
    a_sorted = sorted(a)
    invmax = (n + 1) * n // 2

    ok = 0
    ng = n
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid
    print(a_sorted[ok])
    return
#Solve
if __name__ == '__main__':
    D()
