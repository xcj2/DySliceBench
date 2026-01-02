import math
n = int(input())
a = list(map(int,input().split()))

def gcdall(a):
	rt = 0
	for i in a:
		rt = math.gcd(rt, i)
		if rt == 1:
			break
	return rt

#GCD(ai, aj)=1 がすべてとは, aの中の素因数に共通のものがないということ

def makediv(n):
	lower_divisors , upper_divisors = [], []
	i = 1
	while i*i <= n:
		if n % i == 0:
			lower_divisors.append(i)
			if i != n // i:
				upper_divisors.append(n//i)
		i += 1
	return lower_divisors + upper_divisors[::-1]

def sieve(n):
	ret = set()
	divlis = [-1]*(n+1)  # 何で割ったかのリスト(初期値は-1)
	flag = [True]*(n+1)
	flag[0] = False
	flag[1] = False
	ind = 2
	while ind <= n:
		if flag[ind]:
			ret.add(ind)
			ind2 = ind**2
			while ind2 <= n:
				flag[ind2] = False
				divlis[ind2] = ind
				ind2 += ind
		ind += 1
	#何で割ったかのリストを取得したいとき, divlisも出力する
	return ret

targ = sieve(n)

def pairwise(a):
	t = set()
	mode = True
	for i in a:
		if i == 1:
			continue
		if i in targ:
			if i in t:
				mode = False
				break
			else:
				t.add(i)
		else:
			k = makediv(i)
			for j in k:
				if j == 1:
					continue
				if j not in t:
					t.add(j)
				else:
					mode = False
					break
		if not mode:
			break
	return mode

if gcdall(a) == 1:
	if pairwise(a):
		print("pairwise coprime")
	else:
		print("setwise coprime")
else:
	print("not coprime")