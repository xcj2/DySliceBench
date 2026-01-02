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

n = onem()


on = []

Ma = 0

for i in range(n):
    kkk = []
    p = onem()
    for j in range(p):
        kkk.append(l())
    on.append(kkk)
for i in range(2**n):
    ppp = '{:015b}'.format(i)
    ppp = list(ppp[15-n:])
    ppp.reverse()
    su = 0
    for r in range(n):
        if ppp[r] == "1":
            su += 1
    f = False
    for j in range(n):
        if ppp[j] == "1":
            for k in range(len(on[j])):
                a,b = on[j][k]
                a -= 1
                if b ^ int(ppp[a]):
                    f = True
                    break
    if not f:
        Ma = max(Ma,su)
print(Ma)




