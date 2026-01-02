#!/usr/bin/python3

import sys

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

bound = 10**9 + 7
def comb(n, k):
    ans = 1
    upto = min(k, n - k)
    for i in range(0, upto):
        ans *= n - i % bound
    for i in range(0, upto):
        ans //= upto - i
    return ans

def solve(n, k, i):
    red = n - k
    blue = k
    nr_how_sep_red = cmb(red + 1, i, bound)
    nr_how_put_blu = cmb(blue - 1, i - 1, bound)
    return nr_how_sep_red * nr_how_put_blu % bound

def main():
    inputs = [int(s) for s in sys.stdin.readline().rstrip().split(" ")]
    n, k = inputs
    for i in range(0, k):
        print(solve(n, k, i + 1))

main()