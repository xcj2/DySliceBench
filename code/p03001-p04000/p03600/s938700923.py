def examD():
    # https://juppy.hatenablog.com/entry/2019/02/18/ARC83_-D_Restoring_Road_Network-_Python_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder
    def warshall_floyd(n, d):
        # d[i][j]: iからjへの最短距離
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d
    N = I()
    A = [LI() for _ in range(N)]
    Dist = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            a, b, r = i, j, A[i][j]
            Dist[a][b] = r
    D = warshall_floyd(N,Dist)
    ans = 0
    for i in range(N):
        for j in range(N):
            cur = D[i][j]
            if i==j:
                continue
            if cur<A[i][j]:
                print(-1)
                return
            if cur==A[i][j]:
                flag = True
                for k in range(N):
                    if k==i or k==j:
                        continue
                    if cur==D[i][k]+D[k][j]:
                        flag = False
                if flag:
                    ans += cur
    print(ans//2)
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
    examD()

"""

"""