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

n,d,a = m()

ppp = [0 for i in range(n)]

aaa = []
lll = []
rrr = []
co = 0
for i in range(n):
    p = l()
    aaa.append([p[0],-(-p[1]//a)])
aaa.sort()
for i in range(n):
    lll.append([aaa[i][0],aaa[i][0]+2*d])
c = 0
ll = 0
po = []
for i in range(n):
    on = aaa[i]
    for j in range(ll,n):
        if lll[j][1] < aaa[i][0] and i > j:
            c -= po[j]
        else:
            ll = j
            break
    if on[1] <= c:
        po.append(0)
        continue
    else:
        co += on[1]-c
        po.append(on[1]-c)
        c += on[1]-c
        
        """
        for j in range(i+1,n):
            if aaa[j][0] <= lll[i][1]:
                aaa[j][1] -= on[1]
            else:
                break
        """
        

print(co)








