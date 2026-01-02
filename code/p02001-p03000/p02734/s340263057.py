def examA():
    N, M = LI()
    ans = N*(N-1)//2 + M*(M-1)//2
    print(ans)
    return

def examB():
    def judge(A):
        #print(A)
        n = len(A)
        for i in range(n//2):
            if A[i]!=A[n-i-1]:
                return False
        return True
    S = SI()
    N = len(S)
    if not judge(S):
        print("No")
        return
    if judge(S[:(N-1)//2]) and judge(S[(N+1)//2:]):
        print("Yes")
    else:
        print("No")
    return

def examC():
    L = I()
    ans = (L/3)**3
    print(ans)
    return

def examD():
    N = I()
    A = LI()
    D = defaultdict(bool)
    C = Counter(A)
    M = 0
    for key,c in C.items():
        M += c*(c-1)//2
    #print(C)
    #print(M)
    ans = [0]*N
    for i in range(N):
        a = A[i]
        c = C[a]
        ans[i] = M -(c*(c-1)//2) + ((c-1)*(c-2)//2)
    for v in ans:
        print(v)
    return

def examE():
    H, W, K = LI()
    S = [SI()for _ in range(H)]
    SH = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        now = 0
        for j in range(W):
            now += int(S[i][j])
            SH[i + 1][j + 1] = SH[i][j + 1] + now

    def calc(a,b,c,d):
        return SH[c][d] - SH[a][d] - SH[c][b] + SH[a][b]

    ans = H+W-2
    mask = 2**(H-1)-1
    for i in range(mask+1):
        cut = [0]
        cur = 0
        for j in range(H-1):
            if i&(1<<j)==(1<<j):
                cut.append(j+1)
                cur += 1
        cut.append(H)
        L = [0]*(len(cut)-1)
        flag = True
        for w in range(W):
            now_L = [0]*(len(cut)-1)
            for s in range(len(cut) - 1):
                n = calc(cut[s], w, cut[s + 1], w + 1)
                now_L[s] = n
                if n+L[s]> K:
                    if n>K:
                        flag = False
                        cur = inf
                        break
                    cur += 1
                    L = [0] * (len(cut))
            if not flag:
                break
            for s in range(len(cut) - 1):
                L[s] += now_L[s]
        if not flag:
            continue
        ans = min(ans,cur)

    print(ans)
    return
"""
2 1 1
1
1
"""# 1

def examF():
    N, S = LI()
    A = LI()
    dp = [[0]*(S+1) for _ in range(N+1)]
    for i in range(N):
        dp[i][0] = 1
    for i in range(N):
        a = A[i]
        for j in range(S+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod2
            if j+a<=S:
                dp[i+1][j+a] += dp[i][j]
                dp[i+1][j+a] %= mod2
    ans = 0
    for i in range(N+1):
        ans += dp[i][S]
        ans %= mod2
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque

def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examF()

"""

"""