import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
Max = sys.maxsize
def l():
	return list(map(int,input().split()))
def m():
	return map(int,input().split())
def s(x):
	a = []
	aa = x[0]
	su = 1
	for i in range(len(x)-1):
		if aa == x[i+1]:
			a.append([aa,su])
			aa = x[i+1]
			su = 1
		else:
			su += 1
	a.append([aa,su])
	return a
def jo(x):
	return " ".join(map(str,x))

n,m = m()

a = []

for i in range(m):
	a.append(l())

p = l()

su = 0
kk = []
for i in range(2**n):
	kk = []
	for j in range(m):
		co = 0
		for k in range(a[j][0]):
			if (i >> (n -(a[j][k+1])) & 1):
				co += 1
		kk.append(co)
	if all(kk[i] % 2 == p[i] for i in range(m)):
		su += 1
print(su)