import sys
sys.setrecursionlimit(10**7)

N,M,K=map(int,input().split())


par=[index for index in range(N+1)]

def root(x):
    global par

    if x==par[x]:
        return x
    else:
        par[x]=root(par[x])
        return par[x]


def same(x,y):
    global par

    if root(x)==root(y):
        return True
    else:
        return False

def unite(x,y):
    global par

    if root(x)!=root(y):
        par[root(x)]=root(y)


friends=[[] for index1 in range(N+1)]
for index2 in range(M):
    a,b=map(int,input().split())
    unite(a,b)
    friends[a].append(b)
    friends[b].append(a)


block=[[] for index3 in range(N+1)]
for index4 in range(K):
    c,d=map(int,input().split())
    block[c].append(d)
    block[d].append(c)


relates=[0]*(N+1)
for i in range(1,N+1):
    relates[root(i)]+=1


Ans=[]
for j in range(1,N+1):
    ans=relates[root(j)]-1    #高速化可能   #1
    for k in friends[j]:
        if same(j,k):
            ans-=1
    for l in block[j]:
        if same(j,l):   #まとめられる
            ans-=1

    Ans.append(ans)

print(*Ans)

