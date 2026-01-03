#A
if False:
    N=int(input())
    E=[int(i) for i in input().split()]
    E.sort()
    s=sum(E)
    if E[-1]<s-E[-1]:
        print('Yes')
    else:
        print('No')
#B
if False:
    N=int(input())
    fac=[]
    for i in range(1,10**6+1000):
        if N%i==0:
            fac.append((i,N//i))
    ans=10**19
    for l,r in fac:
        ans=min(l-1+r-1,ans)
    print(ans)
  
#C
if False:
    N=int(input())
    S=[input() for _ in range(N)]
    march=list('MARCH')
    nam=[[] for _ in range(len(march))]
    for s in S:
        if s[0] in march:
            nam[march.index(s[0])].append(s)
    ans=0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                ans+=len(nam[i])*len(nam[j])*len(nam[k])
    print(ans)

#D
if False:
    import sys

    if sys.getrecursionlimit()<10**7:
        sys.setrecursionlimit(10**7)

    N=int(input())
    ver=[[] for _ in range(N)]
    for _ in range(N-1):
        u,v,W=map(int,input().split())
        ver[u-1].append((v-1,W))
        ver[v-1].append((u-1,W))
    his=[-1 for _ in range(N)]

    def dfs(i,col):
        his[i]=col
        for j,w in ver[i]:
            if his[j]==-1:
                if w%2==0:
                    dfs(j,col)
                else:
                    dfs(j,(col+1)%2)

    dfs(0,0)            
    for i in range(N):
        print(his[i])

#E
N,A,B=map(int,input().split())
H=[int(input()) for _ in range(N)]

def ceil(a,b):
    return (a+b-1)//b

def eno(T):
    nee=0
    td=B*T
    dd=A-B
    for h in H:
        if h-td>0:
            nee+=ceil(h-td,dd)
    return nee<=T

l,r=0,10**9+7
while l+1<r:
    mid=(l+r)//2
    if eno(mid):
        r=mid
    else:
        l=mid
print(r)
