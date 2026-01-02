def examA():
    C = SI()
    ans = chr(ord(C)+1)
    print(ans)
    return

def examB():
    N,K,M = LI()
    A = LI()
    ans = N*M-sum(A)
    if ans>K:
        ans = -1
    elif ans<0:
        ans = 0
    print(ans)
    return

def examC():
    N, M = LI()
    ansT = 0; ansP = 0
    d = defaultdict(bool)
    WA = [0]*(N+1)
    for i in range(M):
        S, P = LSI()
        S = int(S)
        if P=="WA":
            WA[S] +=1
        elif P=="AC":
            if d[S]:
                continue
            else:
                d[S] = True
                ansT +=1
                ansP +=WA[S]
    print(ansT,ansP)
    return


def bfs_grid(h,w,s,maze):
    distance = [[-1]*w for _ in range(h)]
    def bfsg():
        queue = deque()
        queue.append(s)
        distance[s[0]][s[1]] = 0
        while len(queue):
            y, x = queue.popleft()
            for i in range(4):
                nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                if (0<= nx <w and 0<= ny <h and maze[ny][nx] != '#'):
                    if distance[ny][nx]<=distance[y][x]+1 and distance[ny][nx]!=-1:
                        continue
                    queue.append((ny, nx))
                    distance[ny][nx] = distance[y][x] + 1
        return distance
    return bfsg()
def examD():
    H,W = LI()
    S = [SI() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                continue
            D = bfs_grid(H, W, [i, j], S)
#            print(D)
            cur = 0
            for d in D:
                cur = max(cur,max(d))
            ans = max(ans,cur)
    print(ans)
    return

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
def examE():
    N, K = LI()
    A = LI(); A.sort()
    maxN = 0; minN = 0
    C = combination(N,mod)
    d = defaultdict(int)
    dL = defaultdict(int)
    for i,a in enumerate(A):
        d[a] +=1
        if d[a]==1:
            dL[a] = i
    for key,i in d.items():
        cur = dL[key]+d[key]
#        print(cur)
        maxN += (C.comb(cur,K,mod)-C.comb(cur-d[key],K,mod))*key
        cur = N-dL[key]
        minN += (C.comb(cur,K,mod)-C.comb(cur-d[key],K,mod))*key
        maxN %=mod
        minN %=mod
#        print(maxN,minN)
    ans = (maxN - minN +mod)%mod
    print(ans)
    return

def examF():
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
    examE()
