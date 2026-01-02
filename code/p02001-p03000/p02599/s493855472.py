#!/usr/bin/env python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def LIR(n):
    res = [None] * n
    for i in range(n):
        l, r = map(int, input().split())
        res[i] = (l - 1, r - 1, i)
    return res

#solve
def solve():
    n, q = LI()
    c = LI()
    lr = [None] * q
    for i in range(q):
        l, r = map(int, input().split())
        lr[i] = (l - 1, r - 1, i)
    ans = [None] * q
    lr.sort(key=lambda x: x[1])
    dp = [-1] * (max(c) + 1)
    bit = [0] * (n + 1)
    def add(i, w):
        """
        i番目にwを加える
        :param int i:
        :param int w:
        :return:
        """
        x = i + 1
        while x <= n:
            bit[x - 1] += w
            x += x & -x
        return
    def sum(i):
        """
        [0,i]の合計
        :param int i:
        :return:
        """
        res = 0
        x = i + 1
        while x > 0:
            res += bit[x - 1]
            x -= x & -x
        return res
    t = 0
    def f(t):
        l, r, j = lr[t]
        xr = sum(r)
        xl = sum(l-1)
        tmp = xr - xl
        ans[j] = tmp
        
    for i in range(n):
        ci = c[i]
        l = dp[ci]
        add(i, 1)
        dp[ci] = i
        if l != -1:
            add(l, -1)
        while t < q and lr[t][1]<= i:
            f(t)
            t += 1
        if t == q:
            break
    for ai in ans:
        print(ai) 
    return


#main
if __name__ == '__main__':
    solve()
