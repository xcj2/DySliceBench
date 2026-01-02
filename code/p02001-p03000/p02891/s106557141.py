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


mod = 1000000007
inf = float('INF')


def A():
    S = input()

    K = II()

    if len(S) == 2:
        print(K//2)
        return

    i = 0
    ans = 0
    A = 1
    p = 0
    z = 0
    z2 = 0
    while(A > 0):
        count = 0
        if i == 0:
            p = 1
        while(S[i] == S[i+1]):

            if S[i+2] == '\n':
                p = 2
            count += 1
            i += 1
        if S[i+1] == '\n':
            p = 2
        if p == 1:
            z = count+1
        if p == 2:
            z2 = count+1

        if(S[i] != S[i+1]):
            i += 1
        if count == len(S)-2:
            print(((len(S)-1)*K)//2)
            return

        if count > 0:
            ans += (count+1)//2

        if S[-1] == S[i]:
            A = -1
        p = 0

    if K >= 2 and S[-2] == S[0] and (z % 2 == 1 and z2 % 2 == 1):
        ans += 1
        print((ans*K)-1)
    else:
        print(ans*K)

    return

# B


def B():
    N, K = map(int, input().split())
    h = LI()
    count = 0

    for i in h:
        if i >= K:
            count += 1
        else:
            continue
    print(count)
    return

# C


def C():
    N = II()
    A = LI()
    J = [0] * N
    for i, n in enumerate(A):
        J[n-1] = i+1
    for s in J:
        print(s, end=" ")

    return

# D


def D():
    A, B = map(int, input().split())
    g = gcd(A, B)
    # go = g
    # myset = set([1])
    sq = int(sqrt(g)) + 2
    ans = 1

    for i in range(2, sq):
        if g % i == 0:
            ans += 1
        while g % i == 0:
            g /= i

            # myset.add(i)
        if g == 1:
            break
        if i == sq - 1:
            # myset.add(go)
            ans += 1

    print(ans)

    return

# E


def E():
    N, M = LI()
    bit_max = 1 << N
    dp = [[inf for i in range(bit_max)] for j in range(M+1)]
    dp[0][0] = 0

    for i in range(M):
        a, b = LI()

        c = LI()
        bit = 0

        for d in c:
            bit |= 1 << (d-1)

        for w in range(bit_max):

            t = w | bit
            cost = dp[i][w] + a

            dp[i+1][t] = min(dp[i+1][t], cost)

            dp[i+1][w] = min(dp[i][w], dp[i+1][w])

    print(-1) if dp[-1][-1] == inf else print(dp[-1][-1])

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
    import math

    vowels = "AIUEO"
    count = 0
    consonants = 0
    newC = []
    newV = []

    for i in S[:-1]:
        if i in vowels:
            count += 1
            newV.append(i)
        else:
            consonants += 1
            newC.append(i)

    if consonants < count or consonants - 2 > count:
        return 0

    a = math.factorial(len(set(newC))) * math.factorial(len(set(newV)))
    return a

    pass


# Solve
if __name__ == '__main__':
    A()
