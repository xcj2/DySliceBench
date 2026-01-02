from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys
import random
import itertools
import math
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


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]


def sosu(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


mod = 1000000007
inf = float('INF')


def A():
    youbi = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    S = input()
    S=S[:-1]
    print(7-youbi.index(S))

    return

# B


def B():
    abc=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    N = II()
    S = input()
    S=S[:-1]
    ans='a'
    for i in S:
        x=abc.index(i)+N
        if x>25:
            x=x-26
        ans+=abc[x]
    ans=ans[1:]
    print(ans)
    return

# C


def C():
    N = II()
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i], y[i] = LI()
    ans = 0
    for j in range(N-1):
        for k in range(j+1, N):
            len = sqrt(((x[j]-x[k])*(x[j]-x[k]))+((y[j]-y[k])*(y[j]-y[k])))
            ans += len
    ans = ans*2/N
    print(ans)

    return

# D


def D():

    a, b, x = LI()
    BIG = a*a*b/2
    if x > BIG:
        y = 2*b-(2*x/a/a)
        print(math.degrees(math.atan(y/a)))
    else:
        y = 2*x/a/b
        print(math.degrees(math.atan(b/y)))
    return

# E


def E():
    N, K = LI()
    A = LI()
    F = LI()
    A.sort(reverse=True)
    F.sort()
    cost = []
    for i in range(len(N)):
        cost.append(A[i]*F[i])

    a = F[cost.index(max(cost))]

    return

# F


def F():
    N, M = LI()

    value = [0] * M
    power = [0] * M
    for i in range(M):
        a, b = LI()
        value[i] = a
        c = LI()
        L = ['0'] * N
        for k in c:
            L[k - 1] = '1'
        bint = ''.join(L)
        power[i] = int(bint, 2)
    bint = ''.join(list(['1'] * N))
    dp = [inf] * (int(bint, 2)+1)
    t = 0
    cost = 0

    dp[0] = 0
    for s in range(int(bint, 2) + 1):
        for i in range(M):
            t = s | power[i]
            cost = dp[s] + value[i]
            dp[t] = min(dp[t], cost)
    print(-1) if(dp[-1] == inf) else print(dp[-1])

    return

    # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6
    N = len(S)

    pass


# Solve
if __name__ == '__main__':
    B()
