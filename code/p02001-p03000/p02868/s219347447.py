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
mod = 998244353
inf = float('INF')

#A
def A():
    n = II()
    n -= 1
    print(n // 2)
    return

#B
def combination_mod(n, k, mod=mod):
    """ power_funcを用いて(nCk) mod p を求める """ 
    """ nCk = n!/((n-k)!k!)を使用 """

    from math import factorial
    if n < 0 or k < 0 or n < k: return 0
    if n == 0 or k == 0: return 1
    a = factorial(n) % mod
    b = factorial(k) % mod
    c = factorial(n - k) % mod
    return (a * pow(b, mod - 2, mod) * pow(c, mod - 2, mod)) % mod
    

def B():
    n = II()
    d = LI()
    dic = defaultdict(int)
    if d[0] != 0:
        print(0)
        return
    for di in d[1:]:
        dic[di] += 1
    ans = 1
    di = list(dic.items())
    di.sort()
    if di[0][0] != 1:
        print(0)
        return
    for i in range(len(di) - 1):
        if di[i][0] != di[i + 1][0] - 1:
            print(0)
            return
    be = 1
    for _, b in di:
        ans *= pow(be, b, mod)
        be = b
        ans %= mod
    print(ans)
    return
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
        i = 1
        s = 0
        step = 1 << (self.size.bit_length() - 1)
        while step:
            if i + step <= self.size and s + self.bit[i + step - 1] < x:
                i += step
                s += self.bit[i - 1]
            step >>= 1
        return i

    def __len__(self):
        return self.size
#C
def C():
    n = II()
    a = LI()
    b = LI()
    tmp = [inf, inf]
    res = None
    for i in range(n):
        if tmp[0] >= b[i] - a[i] >= 0 and b[i] < tmp[1]:
            res = i
            tmp = [b[i] - a[i], b[i]]
    if res == None:
        print("No")
        return
    del a[res]
    del b[res]
    a.sort()
    b.sort()
    ans = 0
    bit = BinaryIndexedTree(b[-1] + 1)
    n -= 1
    for i in range(n):
        tmp = bisect_right(a, b[i]) - bit.sum(b[i])
        bit.add(b[i],1)
        if tmp <= 0:
            print("No")
            return
    print("Yes")

    return

from heapq import heappush, heappop

def Dijkstra(num, start, vedge):

    dist = [float("inf") for i in range(num)]
    dist[0] = 0
    for i in range(num):
        du = dist[i]
        l = i
        for k, j in vedge[i]:
            if dist[j] <= du + k:
                continue
            for j in range(j, i - 1, -1):
                if dist[j] > du + k:
                    dist[j] = du + k
                    continue
                break
    return dist


#D
def D():
    n, m = LI()
    dist = [[] for i in range(n)]
    for _ in range(m):
        l, r, c = LI_()
        c += 1
        dist[l].append([c, r])
    for i in range(n):
        dist[i].sort()
    dist = Dijkstra(n, 0, dist)
    print(dist[n - 1] if dist[n - 1] != inf else -1)
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    D()
