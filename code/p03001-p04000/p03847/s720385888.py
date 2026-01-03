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
    a = LS()
    if a[1][0] == "+":
        print(int("".join(a[0])) + int("".join(a[2])))
    else:
        print(int("".join(a[0])) - int("".join(a[2])))
    return

#B
def B():
    _ = II()
    t = LI()
    tsum = sum(t)
    for _ in range(II()):
        p, x = LI()
        print(tsum - t[p - 1] + x)
    return

#C
def C():
    n = II()
    a = LI()
    d = defaultdict(int)
    ans = 1
    if n & 1:
        for i in a:
            if i & 1:
                print(0)
                return
            d[i] += 1
        for a, b in d.items():
            if a:
                if b == 2:
                    ans *= 2
                    ans %= mod
                    continue
                print(0)
                return
            if b == 1:
                continue
            print(0)
            return
    else:
        for i in a:
            if i & 1:
                d[i] += 1
                continue
            print(0)
            return
        for a, b in d.items():
            if b == 2:
                ans *= 2
                ans %= mod
                continue
            print(0)
            return
    print(ans)
            
        
    return

#D
def D():
    n = II()
    binmax = len(bin(n)) - 2
    dp = [[0] * 3 for i in range(binmax + 1)]
    dp[0][0] = 1
    for i in range(binmax):
        if (n >> binmax - i - 1) & 1:
            # nについて2進数のとき左からibit目が立つ

            # 前bit迄決めた時の和の差が0で今回bitが立つため
            # a,bのここのbitどちらかを立たせると和の差が0
            dp[i + 1][0] = dp[i][0] % mod

            # 前bitを決めた時の和の差が0で今回bitが立つため
            # a,bのここのbitを0にすると和の差が1 dp[i][0]
            # 前bitを決めた時の和の差が1で今回bitが立つため
            # この時点での和の差が3あるため
            # a,bのここのbitを1にすると和の差が1 dp[i][1]
            dp[i + 1][1] = (dp[i][0] + dp[i][1]) % mod

            # 前bitを決めた時の和の差が1で今回bitが立つため
            # この時点での和の差が3あるため
            # a,bのここのbitを(0,1),(0,0)にすると和の差が2以上
            # (0,1)と(1,0)は同じものなので dp[i][1]
            # 前bitを決めた時の和の差が2以上で今回bitが立つため
            # この時点での和の差が4以上あるため
            # 何をしても差は2以上で3通り dp[i][2]
            dp[i + 1][2] = (2 * dp[i][1] + 3 * dp[i][2]) % mod
        else:
            # nについて2進数のとき左からibit目が立たない

            # 前bit迄決めた時の和の差が0で今回bitが立たないため
            # a,bのここのbitを立たせないと和の差が0 dp[i][0]
            # 前bit迄決めた時の和の差が1で今回bitが立たないため
            # この時点での和の差が2あるため
            # a,bのここのbitを立たせると和の差が0 dp[i][1]
            dp[i + 1][0] = (dp[i][0] + dp[i][1]) % mod

            # 前bit迄決めた時の和の差が1で今回bitが立たないため
            # この時点での和の差が2あるため
            # a,bのここのbitをどちらかを立たせると和の差が1 dp[i][1]
            dp[i + 1][1] = dp[i][1] % mod

            # 前bitを決めた時の和の差が1で今回bitが立たないため
            # この時点での和の差が2あるため
            # a,bのここのbitを(0,0)にすると和の差が2以上 dp[i][1]
            # 前bitを決めた時の和の差が2以上で今回bitが立たないため
            # この時点での和の差が4以上あるため
            # 何をしても差は2以上で3通り dp[i][2]
            dp[i + 1][2] = (dp[i][1] + 3 * dp[i][2]) % mod

    print(sum(dp[-1]) % mod)

    return


#Solve
if __name__ == '__main__':
    D()
