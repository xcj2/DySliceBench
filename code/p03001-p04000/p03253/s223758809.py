import sys
input = sys.stdin.buffer.readline

def main():
	K,M = map(int,input().split())
	
	def factorize(n):
		fct = []  # prime factor
		b, e = 2, 0  # base, exponent
		while b * b <= n:
			while n % b == 0:
				n = n // b
				e = e + 1
			if e > 0:
				fct.append((b, e))
			b, e = b + 1, 0
		if n > 1:
			fct.append((n, 1))
		return fct
	
	N = 10**5+100
	MOD = 10**9+7
	fac = [0]*(N+1)
	fac[0],fac[1] = 1,1
	invfac = [0]*(N+1)
	invfac[0],invfac[1] = 1,1

	for i in range(2,N+1):
		fac[i] = (fac[i-1]*i)%MOD

	invfac[-1] = pow(fac[-1],MOD-2,MOD)
	for i in range(N,0,-1):
		invfac[i-1] = (invfac[i]*i)%MOD

	def coef(x,y):
		num = ((fac[x]*invfac[y])%MOD)*invfac[x-y]%MOD
		return num
	
	fl = factorize(M)
	
	ans = 1
	for pr,cnt in fl:
	    ans *= coef(K+cnt-1,K-1)
	    ans %= MOD
	
	print(ans)
	
if __name__ == "__main__":
	main()
