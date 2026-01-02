import sys
#import collections as col
input=sys.stdin.readline

def facto(x, y, mod):
	re = 1
	for i in range(y, x+1):
		re *= i
		re %= mod
	print(re, file=sys.stderr)
	return re

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    #r = min(r, n-r)
    return facto(n, n-r+1, mod) * g2[r] % mod
    #return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
NN = 2 * 10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


def main():
	N,A,B=map(int,input().split())
	#N=input().rstrip()
	#N=int(input())
	#vA=list(map(int,input().split()))
	M = 10**9 + 7
	
	res = pow(2, N, M) - 1
	res = (res+M) % M
	res -= cmb(N, A, M)
	res = (res+M) % M
	res -= cmb(N, B, M)
	res = (res+M) % M
	
	print(res)


main()
