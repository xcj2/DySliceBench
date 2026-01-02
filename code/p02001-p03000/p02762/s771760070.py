n,m,k=[int(j) for j in input().split()]
par=[-1 for i in range(n)]    #par<0なら自身が親で要素の個数、>0なら子で親の位置示す

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


f=set(tuple(int(j)-1 for j in input().split()) for _ in range(m))
b=set(tuple(int(j)-1 for j in input().split()) for _ in range(k))

for a in f:
    if root(a[0])!=root(a[1]):
        connect(a[0],a[1])

ans=[]
for i in range(n):
    ans.append(-par[root(i)]-1)

for i,j in f:
    if root(i)==root(j):
        ans[i]-=1
        ans[j]-=1
for i,j in b:
    if root(i)==root(j):
        ans[i]-=1
        ans[j]-=1

print(*ans)

