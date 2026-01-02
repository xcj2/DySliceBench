import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
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

n,t = m()

li = [l() for i in range(n)]

ma = []
for i in range(n):
    ma.append([li[i][1],i])

ma.sort(reverse = True)

li.sort(key = lambda x:x[0])

dp = [0 for i in range(t + 3000)]

for i in range(n):
    for k in range(li[i][0]+t-1,li[i][0]-1,-1):
        if dp[k] <= dp[k-li[i][0]] + li[i][1]:
            dp[k] = dp[k-li[i][0]] + li[i][1]


dp.sort(reverse = True)
ans = dp[0]

print(ans)


