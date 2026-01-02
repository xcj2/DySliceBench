def bfs(n,e,fordfs):
    #点の数、スタートの点、有向グラフ
    W = [-1]*n
    #各点の状態量、最短距離とか,見たかどうかとか
    W[e] = 0
    que = deque()
    que.append(e)
    len = [float("inf")]*n
    len[e] = 0
    while que:
        now = que.popleft()
        nowv = W[now]
        nowlen = len[now]
        for ne in fordfs[now]:
#            if nowv == W[ne]:
                #ループが嫌な時
#                return -1
            if W[ne] == -1:
                W[ne] = (nowv+1) % 2
                len[ne] = nowlen+1
                que.append(ne)
    return len
def examC(inf):
    N, M = LI()
    ab = [[] for i in range(M)]
    for i in range(M):
        ab[i] = LI()
    cur = 0
    for i in range(M):
        v = [[] for i in range(N)]
        for j in range(M):
            if j!=i:
                v[ab[j][0] - 1].append(ab[j][1] - 1)
                v[ab[j][1] - 1].append(ab[j][0] - 1)
        B  = bfs(N,0,v)
#        print(B)
        if inf in B:
            cur +=1
    print(cur)

import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examC(inf)
