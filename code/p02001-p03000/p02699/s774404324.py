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


def LS(): return list(map(str, input().split()))


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
    S, W = LI()
    if S>W:
        print('safe')
    else:
        print('unsafe')

    
    return

# B


def B():
    A=input().rstrip()
    ans='x'
    for i in range(len(A)-1):
        ans+='x'
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


def D():
    N,K=LI()
    P=LI()
    tmp=sum(P[:K])
    s=0
    pp=sorted(P, reverse=True)
    tmpmax=sum(pp[:K])
    for i in range(K,N+1):
        if (P[i-1]>P[s-1] and s!=0):
            tmp2=sum(P[s:i])
            if (tmp2==tmpmax):
                tmp=tmp2
                break
            tmp=max(tmp,tmp2)
        s+=1
        

    print((tmp+K)/2)
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
