S=input()
n=len(S)
b=[]
a=[]
for i in range(n-1):
    if S[i]=='R' and S[i+1]=='L':
        b.append(i)
def lb(x):
    l=0;r=len(b)-1
    re=0
    while r>=l:
        mid=(l+r)//2
        if b[mid]>=x:
            re=b[mid]
            r=mid-1
        else:
            l=mid+1
    return re
def ub(x):
    l=0;r=len(b)-1
    re=0
    while r>=l:
        mid=(l+r)//2
        if b[mid]<=x:
            re=b[mid]
            l=mid+1
        else:
            r=mid-1
    return re
for i in range(n):
    if S[i]=='R':
        a.append(lb(i))
    else:
        a.append(ub(i))
def Dis(x):
    if S[x]=='R':
        return a[x]-x
    else:
        return x-a[x]-1
dis=list(map(Dis,range(0,n)))
ans=[0 for i in range(0,n)]
for i in range(n):
    if S[i]=='R':
        if (dis[i]&1)==1:
            ans[a[i]+1]+=1
        else:
            ans[a[i]]+=1
    else:
        if (dis[i]&1)==1:
            ans[a[i]]+=1
        else:
            ans[a[i]+1]+=1
for i in ans:
    print(i,end=' ')
