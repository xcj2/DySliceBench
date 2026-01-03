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



import heapq

def dijkstra():
    #n:辺数,w:スタート一
    #n,w = map(int,input().split())
    n = onem()
    edge = [[] for i in range(n)]
    dg = 10**7
    # edge[i]:[コスト]
    for i in range(n-1):
        x,y,z = map(int,input().split())
        x -= 1
        y -= 1
        edge[x].append(z*dg + y)
        edge[y].append(z*dg + x)
    q,w = m()
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

    

    for i in range(q):
        x,y = m()
        print(d[x-1]+d[y-1])


def warshall_floyd(n,d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

dijkstra()
