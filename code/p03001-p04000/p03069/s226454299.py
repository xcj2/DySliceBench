#!usr/bin/env python3
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
mod = 998244353
inf = float('INF')

#A
def A():
    a, b, c = LI()
    if b < a:
        a,b = b,a
    if a <= c <= b:
        print("Yes")
    else:
        print("No")
    return

#B
def B():
    n = II()
    s = input()
    a = list(set(list(s)))
    k = II()-1
    for i in a:
        if s[k] != i:
            s = s.replace(i, "*")
    print(s)
    return

#C
def C():
    n = II()
    s = S()
    dp = [0 for i in range(n)]
    a, b = 0, 0
    for num,i in enumerate(s):
        if i == "#":
            dp[num] += 1
    for i in range(1, n):
        dp[i] += dp[i - 1]
    ans = min(s.count("#"),s.count("."))
    shap = s.count("#")
    for i in range(n):
        a = dp[i] + (n - (i+1) - dp[-1] + dp[i])
        ans = min(ans, a)
    print(ans)


    """
    dp = []
    bf = s[0]
    del s[0]
    a = 
    flg = False
    if bf == ".":
        flg = True
    for i in s:
        if i == bf:
            a += 1
        else:
            dp.append(a)
            a = 1
            bf = i
    dp.append(a)
    a, b = 0, 0
    if flg:
        dp[0] = 0
    if len(s) and s[-1] == "#":
        dp[-1] = 0
    for d in range(len(dp) - 2, -1, -2):
        a += dp[d]
    for d in range(len(dp) - 1, -1, -2):
        b += dp[d]
    print(dp)
    print(min(a,b))
    """
    return

#D
def D():
    n = II()
    ai = IR(n)
    ai.sort()
    ruiseki = [0 for i in range(n)]
    for num, a in enumerate(ai):
        ruiseki[num] = a + ruiseki[num-1]
    select = list(itertools.combinations(range(n), 3))
    ans = 0
    for a,b,c in select:
        A = ruiseki[a]
        B = ruiseki[b] - ruiseki[a]
        C = ruiseki[c] - ruiseki[b]
        if A + B > C and B + C > A and A + C > B:
            ans += 6
            ans = ans % mod
    print(ans)
    
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
    C()
