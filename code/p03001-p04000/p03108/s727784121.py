N,M=map(int,input().split())
parent=[-1 for _ in range(N)]
A=[0]*M
B=[0]*M
ans=[0]*M
ans[M-1]=(N*(N-1))//2

def root(a):
    if parent[a]<0:
        return a
    else:
        parent[a]=root(parent[a])
        return parent[a]


def size(a):
    return -parent[root(a)]

def connect(a,b):
    ra=root(a)
    rb=root(b)

    if ra==rb:
        return False

    if size(ra)<size(rb):
        ra,rb = rb,ra

    parent[ra]+=parent[rb]
    parent[rb]=ra

    return True

for i in range(M):
    A[i],B[i]=map(int,input().split())
    A[i]-=1
    B[i]-=1

for i in range(M-1,0,-1):
    ans[i-1]=ans[i]
    if root(A[i])!=root(B[i]):
        ans[i-1]-=size(A[i])*size(B[i])
        connect(A[i],B[i])

for a in ans:
    print(a)