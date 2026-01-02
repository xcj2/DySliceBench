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

N,K = m()

a = l()


aaa = [0 for i in range(N+1)]
aaa[1] = a[0] % K
for i in range(1,N):
    aaa[i+1] = aaa[i] + a[i]

count = 0
ddd = dict()
ddd[0] = 1
if K == 1:
    print(0)
else:
    for i in range(1,N+1):
        ppp = (aaa[i] - i)%K
        count += ddd.get(ppp,0)
        ddd[ppp] = ddd.get(ppp,0) + 1
        if i - K + 1 >= 0:
            ddd[(aaa[i-K+1] - i + K - 1)%K] -= 1
    print(count)








