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
    K, X= LI()

    if (500*K>=X):
        print('Yes')
    else:
        print('No')


    return

# B


def B():
    N=II()
    S=input()
    ans=0
    s=0
    for i in S:
        if (i=="A" and S[s+1]=='B' and S[s+2]=='C'):
            ans+=1
        s+=1
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

def jisyo(P):
    i=1
    S = sorted(P)
    X=0
    N=len(P)
    for p in P:
    
        X+=((S.index(p)+1) * (math.factorial(N-i)))-1
        
        S.remove(p)
        if len(S)==1:
            break
        i+=1
    return X

def C():
    N=II()
    P=LI()
    Q=LI()

    X=jisyo(P)
    Y=jisyo(Q)


    print(abs(X-Y))
        
    return


# D
def D():
    N, K = LI()
    R, S, P = LI()
    T=list(input().rstrip())
    ans = 0
    for j in range(K):
        if T[j] == 'r':
            ans += P
        if T[j] == 'p':
            ans += S
        if T[j] == 's':
            ans += R
    j = 0
    rps=['r','p','s']

    for i in range(K, N):
        if T[j] == T[i]:
            if i+K>=N:
                j += 1
                continue
            T[i]=rps[rps.index(T[i+K])-1]
            j += 1
            continue
        if T[i] == 'r':
            ans += P
        if T[i] == 'p':
            ans += S
        if T[i] == 's':
            ans += R
        j += 1
    print(ans)
    return


def Dsyakutori():

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
            if (Temp >= K):
                ans += 1

            elif(c < ckeep and i >= 0):
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
    N, M= LI()
    A = LI()
    A.sort(reverse=True)
    B=[0]*(N+1)
    for i in range(1,N+1):
        B[i]=B[i-1]+A[i-1]
    D=[0]*(2*10**5+1)
    for i in range(N):
        D[A[i]]+=1
    for i in range(len(D)-1,0,-1):
        D[i-1]+=D[i]
    l=-1
    r=2*10**5+1
    while r-l>1:
        m=(l+r)//2
        s=0
        for i in range(N):
            s+=D[max(1,m-A[i])]
        if s>=M:
            l=m
        else:
            r=m
    ans=0
    s=0
    for i in range(N):
        v=max(0,r-A[i])
        t=max(0,min(D[v],M-s))
        ans+=B[t]+t*A[i]
        s+=t
    ans+=l*(M-s)
    print(ans)

    
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
