import sys,collections as cl,bisect as bs,copy
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

c = l()

n = onem()

cc = []

for i in range(4):
    cc.append([c[i],i])

cc[-1][0] /= 2

cc[0][0] *= 4
cc[1][0] *= 2



cc.sort()

su = 0

i = 0
while n:
    kkk = cc[i][1]
    if kkk == 0:
        su += 4 * c[kkk] * n
        n = 0
    elif kkk == 1:
        su += 2 * c[kkk] * n 
        n = 0
    elif kkk == 2:
        su += c[kkk]*n
        n = 0
    else:
        su += c[kkk] * (n//2)
        n %= 2
    i += 1
print(su)







