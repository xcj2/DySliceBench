n,m=map(int,input().split())
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

a=[]
for i in range(m):
    a.append([int(j)-1 for j in input().split()])

ans=0
for i in range(m):
    par=[-1 for i in range(n)] 
    for j in range(m):
        if j==i:
            continue
        if root(a[j][0])!=root(a[j][1]):
            connect(a[j][0],a[j][1])
    if -1*min(par)!=n:
        ans+=1
print(ans)


