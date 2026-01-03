def examA():
    O = SI()
    E = SI()
    ans = ""
    for i in range(len(O)+len(E)):
        if i%2==0:
            ans += O[i//2]
        else:
            ans += E[i//2]
    print(ans)
    return

def examB():
    A = LI()
    A.sort()
    ans = (A[2] - A[0]) // 2 + (A[2] - A[1]) // 2
    if (A[2]-A[0])%2==1:
        ans += 1
        if (A[2]-A[1])%2==0:
            ans += 1
    elif (A[2]-A[1])%2==1:
        ans += 2
    print(ans)
    return

def examC():
    S = SI()
    S.replace("RL","A")
    S.replace("LR","B")
    N = len(S)
    A = [0]*N
    print(S)
    l = 0; r = 0
    for i,s in enumerate(S):
        if s=="A":
            A[i] += r
        elif s=="B":
            A[i] += l
    ans = 0
    print(ans)
    return

def examD():
    def warshall_floyd(n, d):
        # d[i][j]: iからjへの最短距離
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d
    H, W = LI()
    C = [LI()for _ in range(10)]
    A = [LI()for _ in range(H)]
    C = warshall_floyd(10,C)
    ans = 0
    for i in range(H):
        for j in range(W):
            a = A[i][j]
            if a==-1:
                continue
            ans += C[a][1]
    print(ans)
    return

def examE():
    N, M = LI()
    V = [[]for _ in range(N)]
    for _ in range(M):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)

    def dfs(s,visited):
        #print(s,visited)
        res = 0
        visited.add(s)
        if len(visited)==N:
            visited.remove(s)
            return 1
        for ne in V[s]:
            if ne in visited:
                continue
            res += dfs(ne,visited)
        visited.remove(s)
        return res

    visited = set()
    ans = dfs(0,visited)
    #print(visited)
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
    examE()

"""

"""