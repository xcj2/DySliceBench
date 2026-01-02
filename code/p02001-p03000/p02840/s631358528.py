def examE():
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

def examF():
    N, X, D = LI()

    if D==0:
        ans = N + 1
        if X==0:
            ans = 1
        print(ans)
        return

    if D<0:
        X, D = -X, -D

    S = defaultdict(list)
    for i in range(N+1):
        base = (X*i) % D
        start = (X*i) // D + i*(i-1)//2
        end = (X*i) // D + i*(N-1 + N -i)//2
        S[base].append([start,end])
    #print(S)

    ans = 0
    for d in S.values():
        d.sort()
        L, R = d[0]
        if len(d)==1:
            ans += R - L + 1
            continue

        for l,r in d[1:]:
            if r<=R:
                continue
            if R<l:
                ans += R - L + 1
                L, R = l, r
            elif R<r:
                R = r
        ans += R - L + 1
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
    examF()
