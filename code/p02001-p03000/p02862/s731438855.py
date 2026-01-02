import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def IS(): return sys.stdin.readline()[:-1]
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LII(rows_number): return [II() for _ in range(rows_number)]
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]

def main():
	X,Y = MI()
	N3 = (2*Y-X)
	M3 = (2*X-Y)
	if(N3%3!=0 or M3%3!=0 or N3 < 0 or M3<0):
		print(0)
	else:
		N=N3//3
		M=M3//3

		K = min(N,M)

		def cmb(n, r, mod):
			if ( r<0 or r>n ):
				return 0
			r = min(r, n-r)
			return g1[n] * g2[r] * g2[n-r] % mod

		mod = 10**9+7 #出力の制限
		L = 10**6
		g1 = [1, 1] # 元テーブル
		g2 = [1, 1] #逆元テーブル
		inverse = [0, 1] #逆元テーブル計算用テーブル

		for i in range( 2, L + 1 ):
			g1.append( ( g1[-1] * i ) % mod )
			inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
			g2.append( (g2[-1] * inverse[-1]) % mod )

		print(cmb(N+M,K,mod))


main()