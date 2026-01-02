def examA():
    S = SI()
    if S[2]==S[3] and S[4]==S[5]:
        print("Yes")
    else:
        print("No")
    return

def examB():
    X = I()
    ans = 0
    ans += (X//500) * 1000
    X %= 500
    ans += (X//5) * 5
    print(ans)
    return

def examC():
    K, N = LI()
    A = LI()
    L = [0]*N
    L[0] = K-A[-1] + A[0]
    for i in range(1,N):
        L[i] = A[i]-A[i-1]
    ans = sum(L) - max(L)
    #print(L)
    print(ans)
    return

def examD():
    def bfs(n, e, fordfs):
        # 点の数、スタートの点、有向グラフ
        W = [-1] * n
        # 各点の状態量、最短距離とか,見たかどうかとか
        W[e] = 0
        que = deque()
        que.append(e)
        while que:
            now = que.popleft()
            nowW = W[now]
            for ne in fordfs[now]:
                if W[ne] == -1:
                    W[ne] = nowW + 1
                    que.append(ne)
        return W
    N, X, Y = LI()
    V = [[]for _ in range(N)]
    for i in range(N-1):
        V[i].append(i+1)
        V[i+1].append(i)
    V[X-1].append(Y-1)
    V[Y-1].append(X-1)
    #print(V)
    ans = [0]*(N-1)
    for i in range(N):
        L = bfs(N,i,V)
        for l in L:
            if l==0:
                continue
            ans[l-1] += 1
    for v in ans:
        print(v//2)
    return

def examE():
    X, Y, A, B, C = LI()
    P = LI()
    Q = LI()
    R = LI()
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)
    cnt = sum(P[:X]) + sum(Q[:Y])
    #print(cnt)
    X -= 1; Y -= 1
    for c in range(C):
        if X>=0 and Y>=0:
            if P[X] <= Q[Y]:
                if P[X] >= R[c]:
                    break
                cnt += (R[c] - P[X])
                X -= 1
            else:
                if Q[Y] >= R[c]:
                    break
                cnt += (R[c] - Q[Y])
                Y -= 1
        elif X>=0:
            if P[X] >= R[c]:
                break
            cnt += (R[c] - P[X])
            X -= 1
        elif Y>=0:
            if Q[Y] >= R[c]:
                break
            cnt += (R[c] - Q[Y])
            Y -= 1
    ans = cnt
    print(ans)
    return

def examF():
    class combination():
        # 素数のmod取るときのみ　速い
        def __init__(self, n, mod):
            self.n = n
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r, mod):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % mod

    N = I()
    V = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
    C = combination(N, mod)

    A = [0]*N
    children = [-1] * N
    ans = [0]*N

    # 子の数のカウント
    def dfs(n, s, edges):
        size = 1
        nowchild = []
        cur = 1
        children[s] = 0
        for i in edges[s]:
            if children[i] != -1:
                continue
            ns, nc = dfs(n, i, edges)
            nowchild.append(ns)
            size += ns
            cur *= nc
            cur %= mod
        children[s] = size
        rest = size - 1
        for k in nowchild:
            cur *= C.comb(rest, k, mod)
            rest -= k
            cur %= mod
        A[s] = cur
        return size, cur

    def dfs2(s,p):
        #print(children, A)
        rep = 1
        rest = N - 1
        for to in V[s]:
            rep *= A[to]
            rep %= mod
        for to in V[s]:
            rep *= C.comb(rest, children[to], mod)
            rest -= children[to]
            rep %= mod
        ans[s] = rep

        n = len(V[s])
        L = [0]*n; R = [0]*n
        L2 = [0]*n; R2 = [0]*n

        for i,ne in enumerate(V[s]):
            L[i] = R[i] = A[ne] * C.inv[children[ne]]
            L2[i] = R2[i] = children[ne]
        for i in range(1,n):
            L[i] *= L[i-1]
            L[i] %= mod
            L2[i] += L2[i-1]
        for i in range(1,n-1)[::-1]:
            R[i] *= R[i+1]
            R[i] %= mod
            R2[i] += R2[i+1]
        for i,ne in enumerate(V[s]):
            if ne==p:
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
            A[s] *= C.fac[N-children[ne]-1]
            A[s] %= mod
            #print(A[s],s,L,R)
            dfs2(ne, s)
        return

    dfs(N, 0, V)
    dfs2(0,-1)
    for v in ans:
        print(v)
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