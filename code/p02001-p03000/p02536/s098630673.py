import sys
input=sys.stdin.readline
n,m=map(int,input().split())
def unite(x,y):
	if same(x,y)==False:
		rx=root(x);ry=root(y)
		if rank[rx]>rank[ry]:
			parent[ry]=rx
			size[rx]+=size[ry]
		else:
			parent[rx]=ry
			size[ry]+=size[rx]
			if rank[rx]==rank[ry]:
				rank[ry]+=1
def root(x):
	if x!=parent[x]:
		return root(parent[x])
	return x
def same(x,y):
	return root(x)==root(y)
parent=list(range(n))
rank=[0]*n
size=[1]*n
for i in range(m):
	a,b=map(int,input().split())
	unite(a-1,b-1)
kind=set()
for i in range(n):
	r=parent[root(i)]
	kind.add(r)
print(len(kind)-1)