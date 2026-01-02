def examA():
    X, Y, Z = LI()
    X, Y = Y,X
    X,Z = Z, X
    print(X,Y,Z)
    return

def examB():
    N, M = LI()
    A = LI()
    need = (sum(A)-1)//(4*M) + 1
    ans = 0
    #print(need)
    for a in A:
        if a>=need:
            ans += 1
    if ans>=M:
        print("Yes")
    else:
        print("No")
    return

def examC():
    N, K = LI()
    ans = N%K
    if K-ans<ans:
        ans = K-ans
    print(ans)
    return

def examD():
    def bfs(n):
        # 点の数、スタートの点、有向グラフ
        W = [""] * n
        # 各点の状態量、最短距離とか,見たかどうかとか
        que = deque()
        for i in range(1,10):
            que.append(str(i))
            W[i-1] = str(i)
        i = 9
        while(i<n):
            now = que.popleft()
            end = now[-1]
            for j in [-1,0,1]:
                ne = int(end)+j
                if 0<=ne<=9:
                    W[i] = now + str(ne)
                    que.append(W[i])
                    i += 1
                    if i==n:
                        break
        return W
    K = I()
    if K<=12:
        ans = K
        print(ans)
        return
    ans = bfs(K)[-1]
    print(ans)
    return

def examE():
    N, K, C = LI()
    S = SI()
    L = set()
    R = set()
    prev = -inf
    for i,s in enumerate(S):
        if s=="x":
            continue
        if prev+C>=i:
            continue
        L.add(i)
        prev = i
    if len(L)>K:
        print()
        return
    prev = inf
    for i in range(N)[::-1]:
        s = S[i]
        if s=="x":
            continue
        if prev-C<=i:
            continue
        R.add(i)
        prev = i
    #print(L,R)
    ans = []
    for i in L:
        if i in R:
            ans.append(i+1)
    if not ans:
        print()
        return
    ans.sort()
    for v in ans:
        print(v)
    return

def examF():
    N = I()

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
    examE()

"""

"""