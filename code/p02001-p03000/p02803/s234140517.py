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

def examE():
    N, K = LI()
    A = LI()

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
    examD()
