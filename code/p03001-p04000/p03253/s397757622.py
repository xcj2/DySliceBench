from collections import Counter
def factorization(n) -> list:
	if n==1:return [1]
	ret = []
	i = 2
	while i*i<=n:
		while n%i==0:
			n //= i
			ret.append(i)
		i += 1
	if n!=1:ret.append(n)
	return ret
	
from operator import mul
from functools import reduce
def cmb(n,r):
	if n < r:return 0
	r = min(n-r,r)
	if r==0:return 1
	u = reduce(mul, range(n, n-r, -1))
	d = reduce(mul, range(1,r+1))
	return u//d

def main():
	n,m = map(int,input().split())
	mod = 10**9+7
	if m==1:
		print(1)
		exit()
	ans=1
	for v in Counter(factorization(m)).values():
		ans*=cmb(n+v-1,v)
		ans%=mod
	print(ans)
	
if __name__=="__main__":main()