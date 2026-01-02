def examA():
    L = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]
    K = I()

    ans = L[K-1]
    print(ans)
    return

def examB():
    H, W = LI()
    if H==1 or W==1:
        print(1)
        return
    ans = H*W//2 + (H*W)%2
    print(ans)
    return

def examC():
    a,b,c = LI()
    if c-(a+b)<=0:
        print("No")
        return
    judge = (c-a-b)**2-4*a*b
    if judge>0:
        print("Yes")
    else:
        print("No")
    return

def examD():
    def bfs(N):
        W = [0]*(5*10**6)
        L = [""]*(5*10**6)
        que = deque()
        que.append(0)
        L[0] = "a"
        W[0] = 0
        flag = True
        ne = 0
        while(flag):
            now = que.popleft()
            nowW = W[now]
            if len(L[now])==N:
                flag = False
                break
            for i in range(W[now]+2):
                ne += 1
                W[ne] = max(nowW,i)
                que.append(ne)
                L[ne] = L[now] + alphabet[i]
        return L
    N = I()
    D = bfs(N)
    for ans in D:
        if not ans:
            break
        if len(ans)<N:
            continue
        print(ans)
    return

def examD2():
    N = I()
    def dfs(n,s,i):
        if len(s)==n:
            return
        for k in range(i+1):
            if len(s)==n-1:
                print(s+alphabet[k])
            dfs(n,s+alphabet[k],max(i,k+1))
        return
    dfs(N,"",0)
    return

def examE():
    def LCS_R(S,T):
        N = len(S); M = len(T)
        dp = [[inf] * (M + 1) for _ in range(N + 1)]
        dp_S = [[""] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = 0
        for i in range(N):
            for j in range(M):
                if S[i] == T[j] or S[i] == "?" or T[j] == "?":
                    dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + 1)
                    if dp[i + 1][j + 1]==dp[i][j] + 1:
                        cur = S[i]
                        if S[i] == "?" or T[j] == "?":
                            cur = "?"
                        dp_S[i+1][j+1] = dp_S[i][j] + cur
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j]+1)
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
                if dp[i + 1][j] == dp[i][j] + 1:
                    dp_S[i + 1][j] = dp_S[i][j] + S[i]
                if dp[i][j + 1] == dp[i][j] + 1:
                    dp_S[i][j + 1] = dp_S[i][j] + T[j]
        dp[N][M] = min(dp[N][M], dp[N-1][M] + 1)
        dp[N][M] = min(dp[N][M], dp[N][M-1] + 1)
        if dp[N][M] == dp[N-1][M] + 1:
            dp_S[N][M] = dp_S[N-1][M] + S[N-1]
        if dp[N][M] == dp[N][M-1] + 1:
            dp_S[N][M] = dp_S[N][M-1] + T[M-1]

        i = N; j = M
        rep = []
        while i > 0 and j > 0:
            if dp[i][j] == dp[i - 1][j]:
                rep.append(S[i-1])
                i -= 1
            elif dp[i][j] == dp[i][j - 1]:
                rep.append(T[j-1])
                j -= 1
            else:
                rep.append(S[i - 1])
                i -= 1
                j -= 1

        return dp,dp_S

    A = SI()
    B = SI()
    C = SI()

    a1,d1 = LCS_R(A,B)
    a2,d2 = LCS_R(B,C)
    a3,d3 = LCS_R(C,A)


    S1,d1 = LCS_R(d1[-1][-1],C)
    S2,d2 = LCS_R(d2[-1][-1],A)
    S3,d3 = LCS_R(d3[-1][-1],B)

    ans = min(S1[-1][-1],S2[-1][-1],S3[-1][-1])
    print(ans)
    return

def examF():
    ans = 0
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
    examD2()

"""

"""