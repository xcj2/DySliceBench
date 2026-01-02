n,m=map(int,input().split())
p=[int(i) for i in input().split()]
l=[0 for i in range(n)]
for i in range(n):
    l[p[i]-1]=i
xy=[]

par=[-1 for i in range(n)]

def root(a):
    if par[a]<0:
        return a
    else:
        return root(par[a])

def size(a):
    return -par[root(a)]

def connect(a,b):
    a=root(a)
    b=root(b)
    if a==b:
        return False
    if size(a)<size(b):
        a,b=b,a
    par[a]+=par[b]
    par[b]=a
    return True

for i in range(m):
    a=[int(j)-1 for j in input().split()]
    xy.append(a)
    if root(a[0])!=root(a[1]):
        connect(a[0],a[1])

ans=0
for i in range(n):
    if root(i)==root(l[i]):
        ans+=1
    
print(ans)   