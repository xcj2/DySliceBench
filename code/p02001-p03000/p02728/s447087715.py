def ABC67_B():
    N, K = LI()
    L = LI()
    L.sort(reverse=True)
    ans = sum(L[:K])
    print(ans)
    return

def ABC100_C():
    def factorization_2(n):
        arr = defaultdict(int)
        temp = n
        i = 2
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt
        if temp != 1:
            arr[temp] = 1
        if arr == []:
            arr[n] = 1
        return arr[2]
    N = I()
    A = LI()
    ans = 0
    for a in A:
        ans += factorization_2(a)
    print(ans)
    return

def ARC68_C():
    X = I()
    ans = 0
    ans += 2*(X//11)
    rest = X%11
    if rest>0:
        ans += 1
    if rest>=7:
        ans += 1
    print(ans)
    return

def ABC49_C():
    S = SI()
    T = {"maerd","remaerd","esare","resare"}
    stack = ""
    for s in S[::-1]:
        stack += s
        if stack in T:
            stack = ""
    if stack:
        print("NO")
    else:
        print("YES")
    return

def ABC142_E():
    N, M = LI()
    A = [0]*M
    C = [[]for _ in range(M)]
    for i in range(M):
        A[i], b = LI()
        C[i] = LI()
    mask = 2**N
    dp = [[inf]*mask for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        key = 0
        for j in C[i]:
            key += 2**(j-1)
        #print(key)
        for now in range(mask):
            dp[i + 1][now] = min(dp[i + 1][now], dp[i][now])
            if key|now==now:
                continue
            dp[i+1][now|key] = min(dp[i+1][now|key],dp[i][now]+A[i])
    if dp[M][mask-1]==inf:
        print(-1)
    else:
        ans = dp[M][mask-1]
        print(ans)
    #print(dp)
    return

def ABC160_F():
    class combination():
        # 素数のmod取るときのみ　速い
        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod

    N = I()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
    C = combination(N,mod)
    children = [-1] * N
    A = [0] * N
    rep = [0] * N
    
    def dfs(s):
        size = 1
        nowchild = []
        cur = 1
        children[s] = 0
        for i in V[s]:
            if children[i] != -1:
                continue
            ns, nc = dfs(i)
            nowchild.append(ns)
            size += ns
            cur *= nc
            cur %= mod
        children[s] = size
        rest = size - 1
        for k in nowchild:
            cur *= C.comb(rest, k)
            rest -= k
            cur %= mod
        A[s] = cur
        return size, cur

    def dfs2(s, p=-1):
        cur = 1
        rest = N - 1
        for to in V[s]:
            cur *= A[to]
            cur %= mod
        for to in V[s]:
            cur *= C.comb(rest, children[to])
            rest -= children[to]
            cur %= mod
        rep[s] = cur

        n = len(V[s])
        L = [0] * n; R = [0] * n
        L2 = [0] * n; R2 = [0] * n

        for i, ne in enumerate(V[s]):
            L[i] = R[i] = A[ne] * C.inv[children[ne]] % mod
            L2[i] = R2[i] = children[ne]
        for i in range(1, n):
            L[i] *= L[i - 1]
            L[i] %= mod
            L2[i] += L2[i - 1]
        for i in range(1, n - 1)[::-1]:
            R[i] *= R[i + 1]
            R[i] %= mod
            R2[i] += R2[i + 1]
        for i, ne in enumerate(V[s]):
            if ne == p:
                continue
            A[s] = 1
            children[s] = 1
            if i > 0:
                A[s] *= L[i - 1]
                A[s] %= mod
                children[s] += L2[i - 1]
            if i + 1 < n:
                A[s] *= R[i + 1]
                A[s] %= mod
                children[s] += R2[i + 1]
            A[s] *= C.fac[N - children[ne] - 1]
            A[s] %= mod
            dfs2(ne, s)
        return

    dfs(0)
    dfs2(0)

    for ans in rep:
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
    ABC160_F()

"""

"""