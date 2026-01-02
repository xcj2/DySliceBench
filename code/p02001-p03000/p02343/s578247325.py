#=============================================================================
# DSL1_A
#=============================================================================
n,q=map(int,input().split())
parents=[i for i in range(n)]
deepth=[0 for _ in range(n)]

def find(x):
    if parents[x]==x:
        return x
    return find(parents[x])

def unite(x,y):
    px=find(x)
    py=find(y)
    if deepth[px]>deepth[py]:
        parents[py]=px
        deepth[px]=max(deepth[px],deepth[py]+1)
    else:
        parents[px]=py
        deepth[py]=max(deepth[py],deepth[px]+1)

def same(x,y):
    if find(x)==find(y):
        return True
    else:
        return False

for _ in range(q):
    com,x,y=map(int,input().split())
    if com==0:
        unite(x,y)
    if com==1:
        if same(x,y):
            print(1)
        else:
            print(0)


