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

mod = 10**9+7 #出力の制限
N = 10**5 * 2
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

import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n,a,b = m()

nn = str(n)[::-1]

co = 1

tw = [[1] for i in range(10)]
for i in range(9):
    tw[0].append(tw[0][-1] * 2)
for i in range(1,10):
    for j in range(9):
        if j == 0:
            tw[i].append((tw[i-1][-1] * tw[i-1][1])%mod)
        else:
            tw[i].append((tw[i][-1]*tw[i][1])%mod)

for i in range(len(nn)):
    if i == 0:
        co *= tw[i][int(nn[i])]
    else:
        co = (co * tw[i][int(nn[i])])%mod
        co = co % mod

aaa = 1
bbb = 1
for i in range(min(a,n-a)):
    aaa *= (n-i)
    aaa %= mod
    if i == min(a,n-a)-1:
        aaa *= g2[i+1]
        aaa %= mod
for i in range(min(b,n-b)):
    bbb *= (n-i)
    bbb %= mod
    if i == min(b,n-b)-1:
        bbb *= g2[i+1]
        bbb %= mod


print((co - aaa - bbb - 1)%mod)

