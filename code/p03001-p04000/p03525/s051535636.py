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


n = onem()

d = l()

d.sort()

a = [0 for i in range(24)]
a[0] += 1

for i in range(n):
    if i % 2 == 0:
        a[d[i]] += 1
    else:
        if d[i]:
            a[24 - d[i]] += 1
        else:
            a[0] += 1

co = 12

for i in range(24):
    if a[i] >= 2:
        co = 0
        break
    for j in range(i+1,24):
        if a[i] >= 1 and a[j] >= 1:
            co = min(co,min(24-(j-i),j-i))
print(co)




