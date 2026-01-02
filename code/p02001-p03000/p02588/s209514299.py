#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n):
    res = [None] * n
    for i in range(n):
        res[i] = II()
    return res
def LIR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LI()
    return res
def FR(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def LIF(n):
    res = [None] * n
    for i in range(n):
        res[i] = IF()
    return res
def SR(n):
    res = [None] * n
    for i in range(n):
        res[i] = S()
    return res
def LSR(n):
    res = [None] * n
    for i in range(n):
        res[i] = LS()
    return res
mod = 1000000007
inf = float('INF')
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

    def search(self, x):
        """
        二分探索。和がx以上となる最小のインデックス(>= 1)を返す
        :param int x:
        :return :
        """
        i = 0
        s = 0
        step = 1 << self.size.bit_length()
        while step:
            if i + step <= self.size and s + self.bit[i + step - 1] < x:
                print(self.bit[i + step - 1], i, step)
                i += step
                s += self.bit[i - 1]
            step >>= 1
        return i

    def __len__(self):
        return self.size
#solve
def solve():
    n = II()
    tmp = []
    ans = 0
    for i in range(n):
        s = S().split(".")
        si = s
        if len(s) == 1:
            s = s[0]
            s = s + "0" * 9
            s = int(s)
        else:
            s0 = s[0]
            s1 = s[1] + "0" * 9
            s = s0 + s1[:9]
            s = int(s)
        t, f = 0, 0
        while s % 2 == 0:
            t += 1
            s //= 2
        while s % 5 == 0:
            f += 1
            s //= 5
        if min(t, f) * 2 >= 18:
            ans -= 1
        tmp.append([t, f, si])
    tmp.sort()
    bitt = BinaryIndexedTree(100)
    r = n - 1
    h = 0
    for i in range(n):
        t, f,_ = tmp[i]
        while r >= 0 and tmp[r][0] + t >= 18:
            bitt.add(tmp[r][1], 1)
            r -= 1
            h += 1
        ans += h - bitt.sum(18 - f - 1)
    print(ans //2)
    return


#main
if __name__ == '__main__':
    solve()
