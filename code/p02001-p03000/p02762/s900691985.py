import sys

sys.setrecursionlimit(6500)

N,M,K=map(int,input().split())

F=[[] for _ in range(N)]
B=[[] for _ in range(N)]
d=[-1]*N

def find(n):
    if d[n]<0:
        return n
    else:
        return find(d[n])
def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:return False
    if d[a]<=d[b]:
        d[a]+=d[b]
        d[b]=a
    else:
        d[b]+=d[a]
        d[a]=b
    return True

def same(a,b):
    if find(a)==find(b):return True
    else:return False


for i in range(M):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    union(a,b)
    F[a].append(b)
    F[b].append(a)

for i in range(K):
    a,b=map(int,input().split())
    B[a-1].append(b-1)
    B[b-1].append(a-1)

ans=[0]*N
for i in range(N):
    p=find(i)
    ans[i]=-d[p]-len(F[i])-1
    for b in B[i]:
        if same(i,b):
            ans[i]-=1
for i in ans:
    print(str(i),end=" ")
