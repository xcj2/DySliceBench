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

import heapq

def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j])
    return d

def warshall_floyd(n,d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d





x,y,a,b,c = m()

al = []

p = l()

q = l()

r = l()

p = [[p[i],1] for i in range(a)]

q = [[q[i],2] for i in range(b)]

r = [[r[i],3] for i in range(c)]



al = []

for i in range(a):
    al.append(p[i])


for i in range(b):
    al.append(q[i])

for i in range(c):
    al.append(r[i])

al.sort(reverse = True)
ans = 0
coa = 0
cob = 0
coc = 0
i = 0

while i <= a+ b+ c:
    on = al[i]
    if on[1] == 1:
        if coa == x:
            i += 1
            continue
        else:
            coa += 1
            ans += on[0]

    elif on[1] == 2:
        if cob == y:
            i += 1
            continue
        else:
            cob += 1
            ans += on[0]

    else:
        coc += 1
        ans += on[0]
    
    if coa + cob + coc == x+y:
        print(ans)
        exit()
    
    i += 1



    