def examA():
    S = SI()
    ans = 0
    if "R" in S:
        ans = 1
    if "RR" in S:
        ans = 2
    if "RRR" in S:
        ans = 3
    print(ans)
    return

def examB():
    N = I()
    L = LI()
    L.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if L[i]==L[j]:
                    continue
                if L[j]==L[k]:
                    continue
                if L[i]+L[j]>L[k]:
                    cnt += 1
    ans = cnt
    print(ans)
    return

def examC():
    X, K, D = LI()
    if X<0:
        X = -X
    ans = inf
    if X>K*D:
        ans = X-K*D
        print(ans)
        return

    K -= X//D
    X -= D * (X//D)

    ans = X
    if K>0:
        if K%2==1:
            ans = abs(X-D)
    print(ans)
    return


def examD():
    N, K = LI()
    P = LI()
    C = LI()

    B = [i for i in range(N)]
    for i, p in enumerate(P):
        p -= 1
        B[i] = p

    locat_doubling = [[0] * N for _ in range(31)]
    score_doubling = [[0] * N for _ in range(31)]

    for i in range(N):
        locat_doubling[0][i] = i
        locat_doubling[1][B[i]] = i
        score_doubling[0][i] = 0
        score_doubling[1][B[i]] = C[i]
    for k in range(2, 31):
        for i in range(N):
            locat_doubling[k][i] = locat_doubling[k - 1][locat_doubling[k - 1][i]]
            score_doubling[k][i] = score_doubling[k - 1][i] + score_doubling[k - 1][locat_doubling[k - 1][i]]

    score = [[-inf for i in range(31)] for _ in range(N)]
    locate = [[i, i] for i in range(N)]
    ans = max(C)
    for i in range(N):
        score[i][0] = 0

    if ans <= 0:
        print(ans)
        return

    for k in range(30)[::-1]:
        for i in range(N):
            if score[i][k] < 0:
                continue
            # print(score[i],locate[i])
            if score_doubling[k + 1][locate[i][1]] > 0:
                score[i][1] += score_doubling[k + 1][locate[i][1]]
                locate[i][1] = locat_doubling[k + 1][locate[i][1]]

        if K & (1 << k) > 0:
            for i in range(N):
                if score[i][k] < score[i][0]:
                    score[i][k] = score[i][0]
                    locate[i][k] = locate[i][0]
                score[i][0] += score_doubling[k + 1][locate[i][0]]
                locate[i][0] = locat_doubling[k + 1][locate[i][0]]

    for s in score:
        ans = max(ans, s[0], s[1])
    print(ans)
    return

def examD2():
    N, K = LI()
    P = LI()
    C = LI()
    checked = [False]*N
    cycle = [[0]*2 for _ in range(N)]

    ans = max(C)
    if ans<=0:
        print(ans)
        return

    for i in range(N):
        if checked[i]:
            continue
        used = [False]*N
        v = i
        cnt = 0
        score = 0
        cycle_use = set()

        while(not used[v]):
            used[v] = True
            cnt += 1
            score += C[v]
            cycle_use.add(v)
            v = P[v]-1

        for i in cycle_use:
            cycle[i] = [cnt, score]
            checked[i] = True

    for i in range(N):
        c,s = cycle[i]
        cur = s * ((K - c) // c)
        if s<0:
            cur = 0
        rest = K - c * ((K-c)//c)
        if ans<cur:
            ans = cur
        now = i
        for _ in range(rest):
            cur += C[now]
            now = P[now] - 1
            if ans<cur:
                ans = cur

    print(ans)
    return

def examE():
    R, C, K = LI()
    V = [[-inf]*C for _ in range(R)]
    for _ in range(K):
        r,c,v = LI()
        V[r-1][c-1] = v
    dp0 = [[0]*(C+1) for _ in range(R+1)]
    dp1 = [[0]*(C+1) for _ in range(R+1)]
    dp2 = [[0]*(C+1) for _ in range(R+1)]
    dp3 = [[0]*(C+1) for _ in range(R+1)]

    for r in range(R):
        for c in range(C):
            v = V[r][c]
            if 0<v:
                dp0[r+1][c+1] = max(dp0[r+1][c],dp0[r][c+1],dp1[r][c+1],dp2[r][c+1],dp3[r][c+1])
                dp1[r+1][c+1] = max(dp1[r+1][c],dp0[r+1][c]+v,dp0[r][c+1]+v,dp1[r][c+1]+v,dp2[r][c+1]+v,dp3[r][c+1]+v)
                dp2[r+1][c+1] = max(dp2[r+1][c],dp1[r+1][c]+v)
                dp3[r+1][c+1] = max(dp3[r+1][c],dp2[r+1][c]+v)
            else:
                dp0[r+1][c+1] = max(dp0[r+1][c],dp0[r][c+1],dp1[r][c+1],dp2[r][c+1],dp3[r][c+1])
                dp1[r+1][c+1] = dp1[r+1][c]
                dp2[r+1][c+1] = dp2[r+1][c]
                dp3[r+1][c+1] = dp3[r+1][c]

    ans = max(dp0[R][C],dp1[R][C],dp2[R][C],dp3[R][C])
    print(ans)
    return

def examF():
    N = I()
    S = ["" for _ in range(N)]
    C = [0 for _ in range(N)]
    for i in range(N):
        s, c = LSI()
        S[i] = s
        C[i] = c

    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examD2()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""