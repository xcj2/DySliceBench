import sys,collections as cl,bisect as bs,heapq as hq
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

n,q = m()

a = l()
a.sort()
d = []
su = 0
co = 0
for i in range(q):
	b,c = m()
	if c > a[0]:
		d.append([b,c])
hq.heapify(a)
d.sort(reverse = True,key = lambda x:x[1])

for i in range(len(d)):
	kk = bs.bisect_left(a,d[i][1])
	if kk == 0:
		break
	else:
		if co + d[i][0] >= kk+1:
			su += d[i][1] * (kk-co)
			co += kk-co
			break
		else:
			su += d[i][0] * d[i][1]
			co += d[i][0]

			
su +=sum(a[co:])
print(su)
