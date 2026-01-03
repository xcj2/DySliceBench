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
            if nowv == W[ne]:
                #ループが嫌な時
                return -1
            elif W[ne] == -1:
                W[ne] = (nowv+1) % 2
                len[ne] = nowlen+1
                que.append(ne)
    return len


def examB():
    N = I()
    v = [[]for _ in range(N)]
    for i in range(N):
        a = I()
        v[i].append(a-1)
    v[1]=[]
    b = bfs(N,0,v)
    if b==-1:
        ans = -1
    else:
        ans = b[1]
    if ans==float("inf"):
        ans = -1
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

examB()
