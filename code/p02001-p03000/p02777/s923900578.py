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
    S, T= LS()
    A,B= LI()
    U= input().rstrip()



    if(S==U):
        print(A-1,B)
    else:
        print(A,B-1)


    
    return

# B


def B():
    N,K,M = LI()
    A = LI()
    ans=M*N- sum(A)
    if ans>K:
        print(-1)
    elif ans<0:
        print(0)
    else:
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


def C():
    N, M = LI()
    P=[]
    S=[]
    count=set([])
    ans=[0]*1000000
    realans=0
    for i in range(M):

        p,s=input().split()
        p=int(p)
        if s=='AC':
            realans+=ans[p]
            count.add(p)
            ans[p]=0
        if s=='WA' and p not in count:
            
            ans[p]+=1
  


    
    print(len(count),realans)
    

        


        

# D


def D():

    H, W= LI()
    S=[]
    d=0
    for i in range(H):
        tmp=input().rstrip()
        c=0
        for j in tmp:
            if '.'==j:
                S.append(d*100+c)
            c+=1
        d+=1
    print(S)



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
