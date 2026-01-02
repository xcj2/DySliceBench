import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
parent=list(range(n))
rank=[0]*n
def root(x):
	if x!=parent[x]:
		x=root(parent[x])
	return x
def same(x,y):
	return root(x)==root(y)
def unite(x,y):
	rx=root(x)
	ry=root(y)
	if rank[rx]<rank[ry]:
		parent[rx]=ry
	else:
		parent[ry]=rx
		if rank[rx]==rank[ry]:
			rank[rx]+=1
f_b=[0]*n
for i in range(m):
	a,b=map(int,input().split())
	unite(a-1,b-1)
	f_b[a-1]+=1
	f_b[b-1]+=1
for j in range(k):
	c,d=map(int,input().split())
	if root(c-1)==root(d-1):
		f_b[c-1]+=1
		f_b[d-1]+=1
p=[0]*n
ans=[]
for i in range(n):
	p[root(i)-1]+=1
for i in range(n):
	r=p[root(i)-1]-f_b[i]-1
	ans.append(r)
print(*ans)