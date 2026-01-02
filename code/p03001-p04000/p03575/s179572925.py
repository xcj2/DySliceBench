#union-findの練習だと思ってやる。
n,m=map(int,input().split())
A=[list(map(int,input().split()))for i in range(m)]

#union_find
#find, sunite, same, sizeを実装する。
def find(x):
    #findはrootを返す
    if par[x]<0:
        return x
    else:
        par[x]=find(par[x])
        return par[x]
def unite(x,y):
    #xとyの属する集合を合体
    #まずは根をとってくる
    x=find(x)
    y=find(y)
    if x==y:
        return False
    else:
        if par[x]>par[y]:
            x,y=y,x
        par[x]+=par[y]
        par[y]=x
def same(x,y):
    #xとyが同じ集合かどうか判定
    return find(x)==find(y)
def size(x):
    return -par[x]
#初期化

c=0
for i in range(m):
    par=[-1]*n
    for j in range(m):
        if i==j:
            r,s=A[j]
            r-=1
            s-=1
        else:
            p,q=A[j]
            p-=1
            q-=1
            unite(p,q)
    if same(r,s)==False:
        c+=1
print(c)