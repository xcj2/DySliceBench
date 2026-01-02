def examA():
    N = I()
    H = LI()
    dp = [inf]*(N)
    dp[0] = 0
    for i in range(N-1):
        dp[i+1] = min(dp[i+1],dp[i]+abs(H[i+1]-H[i]))
        if i<N-2:
            dp[i + 2] = min(dp[i + 2], dp[i]+abs(H[i + 2] - H[i]))
    ans = dp[-1]
    print(ans)
    return

def examB():
    N, K = LI()
    H = LI()
    dp = [inf]*N
    dp[0] = 0
    for i in range(N):
        for k in range(1,K+1):
            if i+k>=N:
                break
            if dp[i+k]>dp[i]+abs(H[i+k]-H[i]):
                dp[i+k] = dp[i]+abs(H[i+k]-H[i])
    ans = dp[-1]
    print(ans)
    return

def examC():
    N = I()
    A = [0]*N; B = [0]*N; C = [0]*N
    for i in range(N):
        A[i],B[i],C[i] = LI()
    dp = [[0]*3 for _ in range(N+1)]
    for i in range(N):
        dp[i+1][0] = max(dp[i][1],dp[i][2]) + A[i]
        dp[i + 1][1] = max(dp[i][0], dp[i][2]) + B[i]
        dp[i + 1][2] = max(dp[i][1], dp[i][0]) + C[i]
    ans = max(dp[N])
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    # https://mzp.hatenadiary.org/entry/20100623/lcs
    # LCS
    def maxBy(f, x, y):
        if f(x) > f(y):
            return x
        else:
            return y
    def lcs(xs, ys, table):
        if (xs, ys) in table:
            return table[(xs, ys)]
        ret = ""
        if xs == "" or ys == "":
            ret = ""
        elif xs[-1] == ys[-1]:
            ret = lcs(xs[:-1], ys[:-1], table) + xs[-1]
        else:
            ret = maxBy(len,
                        lcs(xs[:-1], ys, table),
                        lcs(xs, ys[:-1], table))
        table[(xs, ys)] = ret
        return ret

    S = SI(); N = len(S)
    T = SI(); M = len(T)

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    ans = []

    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])

    i = N; j = M
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j-1]:
            j -= 1
        else:
            ans.append(S[i-1])
            i -= 1
            j -= 1
    print("".join(ans[::-1]))
    return

def examG():

    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""

"""