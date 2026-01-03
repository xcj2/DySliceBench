def examA():
    def calc_L(x1,y1,x2,y2):
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    N = I()
    X = [LI()for _ in range(N)]
    ans = 0
    for x in itertools.permutations(X):
        cur = 0
        for i in range(1,N):
            cur += calc_L(x[i-1][0],x[i-1][1],x[i][0],x[i][1])
        #print(x,cur)
        ans += cur
    for i in range(1,N+1):
        ans /= i
    print(ans)
    return

def examB():
    def judge(n):
        sn = 0
        for i in n:
            sn += int(i)
        if int(n)%sn==0:
            return "Yes"
        return "No"
    N = SI()
    ans = judge(N)
    print(ans)
    return

def examC():
    N, K = LI()
    P = LI()
    ans = 0
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i]+(P[i]+1)/2
    for i in range(N-K+1):
        cur = S[i+K] - S[i]
        if cur>ans:
            ans = cur
    print(ans)
    return

def examD():
    def bfs(n,V,s,W):
        visited = [False]*n
        que = deque()
        que.append(s)
        while(que):
            now = que.pop()
            visited[now] = True
            for ne in V[now]:
                if visited[ne]:
                    continue
                W[ne] += W[now]
                que.append(ne)
        return W
    N, Q = LI()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
    W = [0] * N
    for _ in range(Q):
        p, x = LI()
        W[p-1] += x
    ans = bfs(N,V,0,W)
    print(" ".join(map(str,ans)))
    return

def examE():
    def bfs(n,edges,s):
        L = [inf]*n
        que = deque()
        que.append(s)
        L[s] = 0
        while(que):
            now = que.popleft()
            for ne in edges[now]:
                if L[ne]>L[now]+1:
                    L[ne] = L[now]+1
                    que.append(ne)
        return L
    N = I()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
    F = bfs(N,V,0)
    S = bfs(N,V,N-1)
    f = 0; s = 0
    for i in range(N):
        if F[i]>S[i]:
            s += 1
        else:
            f += 1
    if f>s:
        print("Fennec")
    else:
        print("Snuke")
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