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
inf = 1e10

# solve
# 解説AC
# いやなぜわからん
# 三段階に分けて個数を数えることができて,
# 1段階目D
# 2段階目DM
# 3段階目DMC
# とすれば考えやすい
# キョウプロ辞めたら？　
def solve():
    n = II()
    s = input().rstrip()
    q = II()
    k = LI()
    for ki in k:
        ans = 0
        d = 0
        dm = 0
        m =0
        for i in range(n):
            if i >= ki:
                if s[-ki +i] == "D":
                    d -= 1
                    dm -= m
                elif s[-ki + i] == "M":
                    m -= 1
            if s[i] == "D":
                d += 1
            elif s[i] == "M":
                m += 1
                dm += d
            elif s[i] == "C":
                ans += dm
        print(ans)
    return


#main
if __name__ == '__main__':
    solve()
