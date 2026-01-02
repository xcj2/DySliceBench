import sys,collections as cl
import collections
Max = sys.maxsize
def l():
	return list(map(int,input().split()))
def m():
	return map(int,input().split())
def s(x):
	a = []
	aa = x[i]
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

n,m = m()

a = l()

aa = [a[0]]
aaa = []
for i in range(n-1):
	aa.append(aa[-1]+a[i+1])

for i in range(n):
	aaa.append(aa[i]%m)

k = collections.Counter()

for i in aaa:
	k[i] += 1

ans = 0
for i in range(n):
	if aaa[i] != 0:
		ans += max(k[aaa[i]]-1,0)
		k[aaa[i]] = k[aaa[i]]-1
	else:
		ans += k[aaa[i]]
		k[aaa[i]] -= 1
print(ans)