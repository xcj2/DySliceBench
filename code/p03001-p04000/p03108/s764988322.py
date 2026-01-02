n,m=map(int,input().split())
pair=[]
uf = [-1]*(n+1)

def root(x):
        if uf[x]<0: 
                return x
        else: 
                uf[x]=root(uf[x])
                return uf[x]

def issame(x,y):
        return root(x)==root(y)

def unite(x,y):
        x=root(x)
        y=root(y)
        if x==y:
                return False
        if uf[x]>uf[y]:
                x,y=y,x
        uf[x]+=uf[y]
        uf[y]=x
        return True

def size(x):
        return -uf[root(x)]


ans=[n*(n-1)//2]

for _ in range(m):
        a,b=map(int,input().split())
        pair.append((a,b))

for i,p in enumerate(reversed(pair)):
        if not issame(p[0],p[1]):               
                ans.append(ans[i]-size(p[0])*size(p[1]))
                unite(p[0],p[1])    
        else:
                ans.append(ans[i])

ans.reverse()
for i in range(m):
        print(ans[i+1])
                