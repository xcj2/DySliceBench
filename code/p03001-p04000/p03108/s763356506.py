N,M=map(int,input().split())
AB=[[0,0] for i in range(M)]
for i in range(M):
    AB[i][0],AB[i][1]=map(int,input().split())
par=[i for i in range(N+1)]
rank=[1 for i in range(N+1)]
hight=[1 for i in range(N+1)]
def Union_Find_find(x):
    global par,rank,hight
    if par[x]==x:
        return x
    else:
        return Union_Find_find(par[x])
def Union_Find_unite(x,y):
    global par,rank,hight
    x=Union_Find_find(x)
    y=Union_Find_find(y)
    if x!=y:
        if hight[x]>hight[y]:
            par[y]=x
            rank[x]=rank[x]+rank[y]
            rank[y]=rank[x]
        else:
            par[x]=y
            rank[x]=rank[x]+rank[y]
            rank[y]=rank[x]
            if hight[x]==hight[y]:
                hight[y]+=1
def Union_Find_same(x,y):
    global par,rank,hight
    return Union_Find_find(x)==Union_Find_find(y)
def ncr(n):
    return n*(n-1)//2
res=[]
res.append(ncr(N))
for i in reversed(range(M)):
    A,B=AB[i][0],AB[i][1]
    if res[-1]!=0:
        if Union_Find_same(A,B):
            res.append(res[-1])
        else:
            res.append(res[-1]-rank[Union_Find_find(A)]*rank[Union_Find_find(B)])
            Union_Find_unite(A,B)
    else:
        res.append(0)
for i in reversed(range(M)):
    print(res[i])
