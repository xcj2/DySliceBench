def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

import itertools

X, Y = two_int()

def comb(n,r,mod, N):
    def cmb(n, r, mod):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod

    mod = 10**9+7 #出力の制限
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, N + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )

    return cmb(n,r,mod)

def calc(a, b, p):
    if b==0:
        return 1
    elif b%2==0:
        d=calc(a,b//2, p)
        return (d*d)%p
    else:
        return (a*calc(a,b-1,p))%p

dan = (X+Y)/3
if dan.is_integer():
    n = int(dan+1)
    k = Y-(n-1)+1
    print(int(comb(n-1,k-1,(10**9+7),X)))
else:
    print(0)