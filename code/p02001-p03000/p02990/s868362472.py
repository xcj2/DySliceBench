mod = 10**9+7
fact=[0 for i in range(0, 200000)]
def precompute():
	fact[0]=1
	for i in range(1, 30000):
		fact[i]=(fact[i-1]*i)%mod
def mexp(a, b):
	res = 1
	while b:
		if b%2!=0:
			res =(res%mod)*(a%mod)
			res = res%mod
		a = (a%mod)*(a%mod)
		a = a%mod
		b=b//2
	return res%mod

def ncr(n , r):
	p = fact[n]
	p = p*(mexp(fact[n-r] , mod-2))
	p=p%mod
	p = p*(mexp(fact[r] , mod-2))
	p=p%mod
	return p

def main():
	precompute()
	n , k = map(int, input().split())
	for i in range(1, k+1):
		now = (ncr(n+1-k, i)%mod)*(ncr(k-1, i-1)%mod)
		now = now%mod
		print(now)

if __name__ =="__main__":
	main()