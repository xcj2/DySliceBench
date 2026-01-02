def examE():
    H, W = LI()
    A = [LI() for _ in range(H)]
    B = [LI() for _ in range(H)]
    Diff = [[0] * W for _ in range(H)]
    M = 0
    for i in range(H):
        for j in range(W):
            m = abs(A[i][j] - B[i][j])
            Diff[i][j] = m
            M += m
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][0] |= (1 << Diff[H-1][W-1])
    for i in range(H):
        for j in range(W):
            here = dp[i][j]
            s = Diff[i][j]
            ni = (here << s) | (here >> s)
            ex = 0
            #溢れる分
            for k in range(1, s + 1):
                if (here >> k) & 1:
                    ex |= (1 << (s - k))
            dp[i + 1][j] |= (ni | ex)
            dp[i][j + 1] |= (ni | ex)
#            print(s,ni,here,ex,dp[i+1][j])

    a = dp[H - 1][W - 1]
    ans = 0
    for k in range(M + 1):
        if (a >> k) & 1:
            ans = k
            break
    print(dp)
    print(ans)
    return

def examE2():
    H, W = LI()
    A = [LI() for _ in range(H)]
    B = [LI() for _ in range(H)]
    dp = [0]*(H*W)
    cur = abs(A[0][0] - B[0][0])
    dp[0] |= (1 << cur)
    for i in range(H):
        for j in range(W):
            now = dp[i*W + j]
            if i < H - 1:
                cur = abs(A[i + 1][j] - B[i + 1][j])
                ni = (now << cur) | (now >> cur)
                ex = 0
                for k in range(1, cur + 1):
                    if (now >> k) & 1:
                        ex |= (1 << (cur - k))
                dp[(i+1)*W +j] |= (ni | ex)
            if j < W - 1:
                cur = abs(A[i][j + 1] - B[i][j + 1])
                ni = (now << cur) | (now >> cur)
                ex = 0
                for k in range(1, cur + 1):
                    if (now >> k) & 1:
                        ex |= (1 << (cur - k))
                dp[i*W +j+1] |= (ni | ex)
    #print(dp[-1])
    ans = inf
    for i,f in enumerate(str(bin(dp[-1]))[::-1]):
        if f=="1":
            ans = i
            break
    print(ans)
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

if __name__ == '__main__':
    examE2()
