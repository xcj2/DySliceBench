import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    if len(x) == 0:
        return []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

def Bellman_Ford(s,n,w,es,ppp):
    #s→iの最短距離
    # s:始点, n:頂点数, w:辺の数, es[i]: [辺の始点,辺の終点,辺のコスト]
    d = [Max] * n
    #d[i] : s→iの最短距離
    d[s] = 0
    po = 0
    while po < 2*N + 2*M:
        update = False
        for p,q,r in es:
        # e: 辺iについて [from,to,cost]
            if d[p] != Max and d[q] > d[p] + r:
                d[q] = d[p] + r
                update = True
                if (ppp[q] != 0 and po > N):
                    d[-1] = None
                    update = False
                    break
        if not update:
            break
        po += 1
    return d

import heapq

def dijkstra(n,w,e):
    #n:辺数,w:スタート一

    edge = [[] for i in range(n)]
    dg = 10**18
    # edge[i]:[コスト]
    for i in e:
        x,y = i
        z = 1
        x -= 1
        y -= 1
        edge[x].append(dg + y)
        
    
    s = w-1
    d = [-1]*n
    
    d[s] = 0

    edgelist = []
    for e in edge[s]:
        heapq.heappush(edgelist,e)

        

    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        v,c = minedge%dg,minedge//dg
        if d[v] >= 0:
            continue
        d[v] = c
        for e in edge[v]:
            vNext = e%dg
            if d[vNext]:
                heapq.heappush(edgelist, (e//dg+d[v])*dg + vNext)

    return d


def warshall_floyd(n,d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d




N,M,P = m()

es = []
ess = []

gr = [[] for i in range(N)]

ok = [0 for i in range(N)]

for _ in range(M):

    x,y,z = map(int,input().split())

    x -= 1
    y -= 1
    es.append([x,y,-z+P])
    gr[y].append(x)


ok[-1] = 1
po = cl.deque([N-1])
while po:
    o = po.popleft()
    
    for i in gr[o]: 
        if not ok[i]:
            po.append(i)
            ok[i] = 1





po = Bellman_Ford(0,N,M,es,ok)


print(-1 if po[-1] == None else -po[-1] if po[-1] <= 0 else 0)


