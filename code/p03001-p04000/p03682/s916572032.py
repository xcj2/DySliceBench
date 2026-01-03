n = int(input())
par,rank = [i for i in range(n+1)],[0 for i in range(n+1)]
def root(x):
	if par[x]!=x: par[x] = root(par[x])
	return par[x]
def unite(x,y):
	x2,y2 = root(x),root(y)
	if x2!=y2:
		if rank[x2]<rank[y2]: par[x2] = y2
		else: par[y2] = x2
		if rank[x2]==rank[y2]: rank[x2]+=1
def same(x,y):
	return root(x)==root(y)
a,b = [],[]
for i in range(n):
	x,y = (int(_) for _ in input().split())
	a.append([x,i])
	b.append([y,i])
a,b,h,ans = sorted(a),sorted(b),[],0
from heapq import heappush,heappop
for i in range(n-1):
	heappush(h,(a[i+1][0]-a[i][0],a[i+1][1],a[i][1]))
	heappush(h,(b[i+1][0]-b[i][0],b[i+1][1],b[i][1]))
while h:
	i,j,k = heappop(h)
	if root(j)!=root(k):
		unite(j,k)
		ans += i
print(ans)