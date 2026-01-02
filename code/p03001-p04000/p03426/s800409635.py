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

h,w,d = m()

dp = [[0,0] for i in range(h*w+1)]

cost = [0 for i in range(h*w+1)]

for i in range(h):
    a = l()
    for j in range(w):
        dp[a[j]] = [i,j]

for i in range(1,d+1):
    co = i
    while True:
        if co+d > h*w:
            break
        cost[co+d] = cost[co] + abs(dp[co+d][0] - dp[co][0]) + abs(dp[co+d][1] - dp[co][1])
        co += d

n = onem()

for i in range(n):
    L,R = m()
    print(abs(cost[R]-cost[L]))

