def bfs(n,e,fordfs):
    #点の数、スタートの点、有向グラフ
    W = [-1]*n
    #各点の状態量、最短距離とか,見たかどうかとか
    W[e] = 0
    que = deque()
    que.append(e)
    len = [0]*n
    while que:
        now = que.popleft()
        nowv = W[now]
        nowlen = len[now]
        for ne in fordfs[now]:
            if nowv == W[ne]:
                #ループが嫌な時
                return -1
            elif W[ne] == -1:
                W[ne] = (nowv+1) % 2
                len[ne] = nowlen+1
                que.append(ne)
    return len

def examD():
    N = I()
    v = [[] for i in range(N)]
    for i in range(N-1):
        a, b = LI()
        v[a-1].append(b-1)
        v[b-1].append(a-1)
    fennec = bfs(N,0,v)
    snuke = bfs(N,N-1,v)
    cur = 0
    for i in range(N):
        if fennec[i]>snuke[i]:
            cur +=1
    if cur>=(N+1)//2:
        ans = "Snuke"
    else:
        ans = "Fennec"
    print(ans)

import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
