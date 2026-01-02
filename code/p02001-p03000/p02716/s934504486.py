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

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

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
a = l()


if n % 2 == 0:
    po = [a[i] for i in range(n)]
    
    for i in range(n-3,-1,-1):
        po[i] += po[i+2]

    ans = sum(a[0::2])
    ans = max(ans,sum(a[1::2]))
    co = 0
    for i in range(0,n,2):
        if i+1 <= n-1:
            ans = max(ans,co+po[i+1])
        else:
            ans = max(ans,co)
        co += a[i]

    print(ans)

else:
    po = [a[i] for i in range(n)]
    mi = [-Max for i in range(n)]
    
    for i in range(n-3,-1,-1):
        po[i] += po[i+2]

    ans = sum(a[1::2])
    ans = max(ans,sum(a[0::2]) - a[-1])
    l1 = [-Max for i in range(n)]
    for i in range(n):
        if i != n-1:
            l1[i] = po[i+1]


    for i in range(n-1,-1,-1):
        if i == n-1:
            continue
        elif i == n-2:
            mi[i] = l1[i]
        else:
            mi[i] = max(mi[i+2]+a[i],l1[i])


    l1 = mi

        
    co = 0

    for i in range(0,n,2):
        if i + 2 <= n-1:
            ans = max(ans,co+l1[i+1],co+po[i+2])
        elif i+1 <= n-1:
            ans = max(ans,co+l1[i+1])
        else:
            ans = max(ans,co)
        
        co += a[i]
    co = 0
    for i in range(1,n,2):
        ans = max(ans,co+po[i+1])
        co += a[i]
    print(ans)







