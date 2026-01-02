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
    v1, v2, v3 =LI()
    v=v1+v2+v3
    if(v>=22):
        print('bust')
    else:
        print('win')
    return

# B


def B():
    S = input()
    S=S[:-1]
    count=0
    for i in range(len(S)//2):
        if (S[i]!=S[-1-i]):
            count+=1

    
    print(count)
    return

# C


def C():
    A, B, X = LI()
    tmp=X//A
    
    i= tmp
    for x in range(tmp):
        #print(len(str(i)))
       
        if B*len(str(i))+(10**(len(str(i))-1))>X:
            i=(10**(len(str(i))-1))


        if (A*i)+(B*len(str(i)))<=X:
            if i>1000000000:
                i=1000000000
            print(i)
            return
        i-=1
    print(0)
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
