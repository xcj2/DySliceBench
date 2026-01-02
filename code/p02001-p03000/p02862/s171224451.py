#Beginner COnetst 145 /2019/11/16
#Probrem A
from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

def calc(x,y):
    if (x*2-y)%3 != 0 or (y*2-x)%3 != 0: return 0
    m = (x*2-y)//3
    n = (y*2-x)//3
    if m < 0 or n < 0:return 0
    #return combinations_count(m+n,m)
    return cmb(m+n,m,mod)

DEBUG = 0

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


X,Y = list(map(int, input().split()))

if DEBUG:print(X,Y)

print(calc(X,Y))
