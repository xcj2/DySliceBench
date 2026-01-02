N,M,K=map(int, input().split())
par=[-1 for _ in range(N)]
nums=[-1 for _ in range(N)]
#実装
def find(x):
    if par[x]<0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def size(x):
    return -par[find(x)]

def unite(x,y):
    x,y=find(x),find(y)
    if x==y:
        return
    if x>y:
        x,y=y,x
    par[x]+=par[y]
    par[y]=x

def same(x,y):
    return find(x)==find(y)


for _ in range(M):
    a1,a2=map(int, input().split())
    a1-=1
    a2-=1
    unite(a1,a2)
    nums[a1]-=1
    nums[a2]-=1

for _ in range(K):
    a1,a2=map(int, input().split())
    a1-=1
    a2-=1
    if same(a1,a2):
        nums[a1]-=1
        nums[a2]-=1


for i in range(N):
    nums[i]+=size(i)

print(" ".join(list(map(str,nums))))