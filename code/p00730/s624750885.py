from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def cut(W,H,s):
    s %= (W+H)
    if 0 <= s <= W:
        return [s,H],[W-s,H]
    elif W <= s <= W+H:
        return [W,s-W],[W,H+W-s]

while True:
    N,W,H = inpl()
    if N == 0 and W== 0:
        break

    #         t ,  S , W , H
    cakes = [[INF,INF,INF,INF] for _ in range(N+5)]
    cakes[0] = [0,W*H,W,H]
    for t in range(N):
        p,s = inpl()
        tp,sp,wp,hp = cakes[p-1]
        c1,c2 = cut(wp,hp,s)
        cakes[p-1] = [INF,INF,INF,INF]
        cakes[N+4] = [t,c1[0]*c1[1],c1[0],c1[1]]
        cakes[N+3] = [t,c2[0]*c2[1],c2[0],c2[1]]
        cakes.sort()

    ans = []
    for t,s,w,h in cakes:
        if t == INF:
            break
        ans.append(s)
    ans.sort()
    print(' '.join(map(str,ans)))

