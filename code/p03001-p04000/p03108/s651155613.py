import sys
input=sys.stdin.readline
n,m=map(int,input().split())
ab=[]
for _ in range(m):
	a,b=map(int,input().split())
	ab.append((a-1,b-1))
ab.reverse()
def same(x,y):
	return root(x)==root(y)
def unite(x,y):
	rx=root(x)
	ry=root(y)
	if rank[rx]<rank[ry]:
		if not same(rx,ry):
			size[ry]+=size[rx]
		parent[rx]=ry
	else:
		if not same(rx,ry):
			size[rx]+=size[ry]
		parent[ry]=rx
		if rank[rx]==rank[ry]:
			rank[rx]+=1
def root(x):
	if x!=parent[x]:
		x=root(parent[x])
	return x
rank=[0]*n
size=[1]*n
parent=list(range(n))
p=n*(n-1)//2
ans=[p]
for a,b in ab:
	if not same(a,b):
		ra=root(a)
		rb=root(b)
		p+=size[ra]*(size[ra]-1)//2
		p+=size[rb]*(size[rb]-1)//2
		unite(a,b)
		ra=root(a)
		e=size[ra]
		p-=e*(e-1)//2
	ans.append(p)
ans.reverse()
for i in range(m):
	print(ans[i+1])