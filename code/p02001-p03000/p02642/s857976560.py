import itertools
from collections import Counter
h = int(input())
if h == 1:
	print(1)
	exit()
a = list(map(int,input().split()))
t = Counter(a)
b = []
for i, j in t.most_common():
	if j == 1:
		b.append(i)
bset = set(a)

def sieve(n):
	ret = []
	divlis = [-1]*(n+1)  # 何で割ったかのリスト(初期値は-1)
	flag = [True]*(n+1)
	flag[0] = False
	flag[1] = False
	ind = 2
	while ind <= n:
		if flag[ind]:
			ret.append(ind)
			ind2 = ind**2
			while ind2 <= n:
				flag[ind2] = False
				divlis[ind2] = ind
				ind2 += ind
		ind += 1
	#何で割ったかのリストを取得したいとき, divlisも出力する
	return ret

k = sieve(1000)

def pfact(m):
	pf = {}
	cnt = 0
	i = k[cnt]
	st = len(k)
	while m > 1 and cnt < st:
		i = k[cnt]
		while m%i == 0:
			pf[i] = pf.get(i,0) + 1
			m //= i
		cnt += 1
	if m>1 : pf[m]=1
	return pf

def makediv(n):
	s = pfact(n)
	k = [range(i+1) for i in s.values()]
	ansl = []
	for i in itertools.product(*k):
		ans = 1
		for n, j in enumerate(s.keys()):
			ans *= (j**i[n])
		ansl.append(ans)
	ansl.sort()
	return ansl

ans = 0
for i in b:
	t=makediv(i)
	t.remove(i)
	mode = 1
	for l in t:
		if l in bset:
			mode = 0
			break
	if mode:
		ans += 1
print(ans)