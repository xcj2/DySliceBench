def examA():
    S, T = LSI()
    A, B = LI()
    U = SI()
    if S==U:
        print(A-1,B)
    else:
        print(A,B-1)
    return

def examB():
    S = SI()
    N = len(S)
    ans = ""
    for i in range(N):
        ans += "x"
    print(ans)
    return

def examC():
    N = I()
    A = LI()
    d = defaultdict(int)
    for a in A:
        d[a] += 1
        if d[a]>=2:
            print("NO")
            return
    print("YES")
    return

def examD():
    N, K = LI()
    P = LI()
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i]+(P[i]+1)/2
    ans = 0
    for i in range(N-K+1):
        cur = S[i+K]-S[i]
        ans = max(ans,cur)
    print(ans)
    return

def examE():
    def ketadp(a,K):
        n = len(a)
        C = [i for i in range(K+1)]
        dp = defaultdict(int)
        dp[0, 0, 0] = 1
        for i, less, k in itertools.product(range(n), (0, 1), C):
            max_d = 9 if less else int(a[i])
            for d in range(max_d + 1):
                less_ = less or d < max_d
                if d==0:
                    dp[i + 1, less_, k] += dp[i, less, k]
                elif k<K:
                    dp[i + 1, less_, k+1] += dp[i, less, k]

        ans = sum(dp[n, less, K] for less in (0, 1))
        return ans
    N = SI()
    K = I()
    ans = ketadp(N,K)
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
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

if __name__ == '__main__':
    examE()

"""

"""