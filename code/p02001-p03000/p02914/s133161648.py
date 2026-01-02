#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    s = input()
    if s == "Sunny":
        print("Cloudy")
    elif s == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")
    return

#B
def B():
    s = S()
    for i in range(len(s)):
        if i%2:
            if s[i] not in ["L","U","D"]:
                print("No")
                return
        else:
            if s[i] not in ["R","U","D"]:
                print("No")
                return
    print("Yes")
    return

#C
def C():
    n,k,q = LI()
    a = IR(q)
    f = [k-q]*(n)
    for i in range(q):
        ai = a[i]-1
        f[ai] += 1
    for i in f:
        if i <= 0:
            print("No")
        else:
            print("Yes")
    return

#D
def D():
    n,m = LI()
    a = LI()
    q = []
    for i in range(n):
        heappush(q,-a[i])
    for i in range(m):
        x = heappop(q)
        x *= -1
        x >>= 1
        heappush(q,-x)
    print(-sum(q))
    return

#E
def E():
    n = I()
    s = S()
    l = 0
    r = n
    M = 10**64+1
    b = 26
    alp = list("abcdefghijklmnopqrstuvwxyz")
    f = {}
    for i in alp:
        f[i] = ord(i)-ord("a")
    pb = [pow(b,i,M) for i in range(n+1)]
    while r-l > 1:
        m = (l+r)>>1
        d = defaultdict(lambda : float("inf"))
        hash = 0
        for i in s[:m]:
            hash *= b
            hash += f[i]
            hash %= M
        d[hash] = 0
        t = pb[m]
        for i in range(n-m):
            si = s[i]
            hash *= b
            hash -= t*f[si]
            hash += f[s[i+m]]
            hash %= M
            if d[hash]+m <= i+1:
                l = m
                break
            if i+1 < d[hash]:
                d[hash] = i+1
        else:
            r = m
    print(l)
    return

#F
def F():
    """
    A := 赤く塗ったもののxor
    B := 青く塗ったもののxor
    S := 全体のxor

    <問題> A^Bの最大化

    A^B = S、およびA+B = A^B+(A&B)*2より
    A+B = S+(A&B)*2、Sは定数であるため、A&Bを最大化すればよい

    ここで、Sのiビット目がたっているときどのように分けてもA&Bは0となるため
    Ajからiビット目をすべて取り払う。これにより、どのような場合も全体のxorは0となり、
    常にA=Bが成り立つ。
    よってAの最大化を考えればよい。

    AはAjのxorの線形結合により生成される集合の要素である。
    ゆえにAjのxorの線形結合で作られる数のうち最大のものを解とすることができる。
    これは上位ビットから優先的にとるようにすれば生成が可能である。
    あとは基本行変形をおこない、解を求めやすい形にして階数の分だけ大きい順にAjをとれば解となる。
    
    """
    n = I()
    m = 60
    b = [1<<i for i in range(m)]
    a = LI()
    s = 0
    for i in a:
        s ^= i
    for i in range(m):
        if s&b[i]:
            for j in range(n):
                if a[j]&b[i]:
                    a[j] -= b[i]
    k = 0
    for j in range(m):
        bj = b[-j-1]
        for i in range(k,n):
            if a[i]&bj:
                break
        else:
            continue
        a[i],a[k] = a[k],a[i]
        for i in range(n):
            if i == k:
                continue
            if a[i]&bj:
                a[i] ^= a[k]

        k += 1
        if k == n:
            break
    ans = 0
    for i in range(k):
        ans ^= a[i]

    print(s+2*ans)
    return

#Solve
if __name__ == "__main__":
    F()
