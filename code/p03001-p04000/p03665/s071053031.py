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
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]
n,p = m()

a = l()

on= 0

su = 0

for i in range(n):
    a[i] %= 2
    if a[i] == 1:
        on += 1
no = n - on

if p % 2 == 0:
    if on % 2 == 0:
        for i in range(0,on+1,2):
            su += cmb(on,i)
        suu = 0
        for i in range(no+1):
            suu += cmb(no,i)
        su *= suu
    else:
        for i in range(1,on+1,2):
            su += cmb(on,i)
        suu = 0
        for i in range(no+1):
            suu += cmb(no,i)
        su *= suu

else:
    if on % 2 == 0:
        for i in range(1,on+1,2):
            su += cmb(on,i)
        suu = 0
        for i in range(no+1):
            suu += cmb(no,i)
        su *= suu

    else:
        for i in range(0,on+1,2):
            su += cmb(on,i)
        suu = 0
        for i in range(no+1):
            suu += cmb(no,i)
        su *= suu

print(su)

