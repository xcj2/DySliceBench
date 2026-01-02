import sys,collections as cl,bisect as bs,heapq as hq
sys.setrecursionlimit(100000)
Max = sys.maxsize
def l():
	return list(map(int,input().split()))
def uy():
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

n,m = uy()

a = l()

su = 0
for i in range(n+1):
	ll = max(i,n-(m - i))
	if ll == i:
		lll = abs(i-n-(m - i))
	else:
		lll = 0

	for j in range(ll,n+1):
		q = []
		co = 0
		p = a[:i]
		pp = a[j:]
		for k in range(len(p)):
			if p[k] < 0:
				hq.heappush(q,p[k])
		for k in range(len(pp)):
			if pp[k] < 0:
				hq.heappush(q,pp[k])
		co += sum(p)
		co += sum(pp)
		q.sort()
		for k in range(min(len(q),j-ll+lll)):
			co += abs(hq.heappop(q))
		su = max(su,co)
print(su)
