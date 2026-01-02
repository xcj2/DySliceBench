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
    a = LI()
    a.sort()
    print(a[0]*a[1]//2)  
    return

#B
def B():
    d = defaultdict(int)
    s = II()
    def f(n):
        if n % 2:
            return 3 * n + 1
        return n // 2
    i = 1
    while not d[s]:
        d[s] = 1
        s = f(s)
        i += 1
    print(i)
    return

#C
def C():
    n = II()
    h = LI()
    ans = h[0]
    for i in range(n - 1):
        ans += max(0, h[i + 1] - h[i])
    print(ans)
    return

# D
# 解説AC
# 大きいものからとっていった際にその種類数をn
# としてi<=nの種類数においてこれを超えるものは無い
# それより大きいものについて種類数が減らずかつとったものの中で
# 一番小さいものを除き、種類数が増える一番大きいものをとってこれば
# i+1番目の種類下でもっとも大きい数になる 
def D():
    n, k = LI()
    ma = []
    for _ in range(n):
        t, di = LI()
        ma.append((di, t))
    ma.sort()
    ma = deque(ma)
    s = defaultdict(int)
    t = 0
    ans = 0
    q = []
    for _ in range(k):
        di,ti = ma.pop()
        ans += di
        heappush(q, (di, ti))
        if not s[ti]:
            t += 1
        s[ti] += 1
    ans += t ** 2
    ans = [ans]
    while ma and q:
        di, ti = ma.pop()
        while s[ti] and ma:
            di, ti = ma.pop()
        if not ma and s[ti]:
            break
        d1, t1 = heappop(q)
        while s[t1] == 1 and q:
            d1, t1 = heappop(q)
        if not q and s[t1] == 1:
            break
        s[t1] -= 1
        tmp = ans[-1]
        tmp = tmp - d1 + di - t ** 2
        t += 1
        tmp += t ** 2
        ans.append(tmp)
        heappush(q, (di, ti))
        s[ti] += 1
    print(max(ans))


    return

#Solve
if __name__ == '__main__':
    D()
