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
    S, T= input().split()
    
    
    print(T+S)

    
    return

# B


def B():
    N, X = LI()
    L = LI()

    ans = 1
    D = 0
    for i in range(2, N+2):
        D = D+L[i-2]
        if (D > X):
            break
        ans += 1
    print(ans)

    return

# C


def true():
    S = input()
    S = S[:-1]

    tmp = 0
    for x in range(1 << (len(S)-1)):
        func = S[-1]
        for i in range(len(S)-1):
            if(x & (1 << i)):
                tmp += int(func)
                func = S[-2-i]
            else:
                func = S[-2-i]+func
        tmp += int(func)
    print(tmp)

    return


def flagcounter(x):
    if (x == 0):
        return 0
    return flagcounter(x >> 1)+(x & 1)


def C():
    W, H, x, y = LI()

    if (W/2 == x and H/2 == y):
        print(W*H/2, 1)
    else:
        print(W*H/2, 0)

    return


# D


def D():

    N, K = LI()
    A = LI()
    MAX = sum(A)
    if MAX < K:
        print(0)
        return
    Temp = MAX
    ans = 1
    for i in range(N):
        Temp = Temp-A[i]
        if (Temp >= K):
            ans += 1
        else:
            T = Temp+A[i]
            break
    Temp = T
    ckeep = N
    for k in range(N):
        c = N-1
        i -= 1
        Temp = T

        for j in range(N):
            Temp = Temp-A[c]
            if (Temp >= K ):
                ans += 1
            
            elif(c < ckeep and i>=0):
                ans += i
                ckeep = c
                break
            else:
                ckeep = c
                break
            c -= 1
        if i < 0:
            break
        T = T+A[i]
    print(ans)

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

    A()
