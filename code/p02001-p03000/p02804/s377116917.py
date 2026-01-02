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
    n,w = map(int,input().split())

    edge = [[] for i in range(n)]
    dg = 10**7
    # edge[i]:[コスト]
    for i in range(n-1):
        x,y = map(int,input().split())
        z = 1
        x -= 1
        y -= 1
        edge[x].append(dg + y)
        edge[y].append(dg + x)
    
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

mod = 10**9+7 #出力の制限
N = 10**5
def cmb(n, r):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
def p(n,r):
    if ( r<0 or r>n ):
        return 0
    return g1[n] * g2[n-r] % mod

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
# a = cmb(n,r)


N,M = m()


a = l()

a.sort()

po = cmb(N,M)

aa = s(a)

cc = 0

count = 0
for i in range(len(aa)):
    cc += aa[i][1]
    count += (cmb(cc,M) - cmb(cc-aa[i][1],M))*aa[i][0]
    count -= (cmb(N-cc+aa[i][1],M) - cmb(N-cc,M))*aa[i][0]
    count %= mod
print(count)























