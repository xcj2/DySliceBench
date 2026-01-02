def n0():return int(input())
def n1():return [int(x) for x in input().split()]
def n2(n):return [int(input()) for _ in range(n)]
def n3(n):return [[int(x) for x in input().split()] for _ in range(n)]

n,m=n1()
sc=n3(m)

d={i:-1 for i in range(1,n+1)}
ans=9999
for i in range(m):
    if d[sc[i][0]]>=0 and d[sc[i][0]]!=sc[i][1]:
        ans=-1
        break;
    else:
        d[sc[i][0]]=sc[i][1]
else:
    if len(d)==3:
        if d[1]==0:
            ans=-1
        if d[1]==-1:d[1]=1
        if d[2]==-1:d[2]=0
        if d[3]==-1:d[3]=0
        if ans!=-1:ans=d[1]*100+d[2]*10+d[3]
    elif len(d)==2:
        if d[1]==0:
            ans=-1
        if d[1]==-1:d[1]=1
        if d[2]==-1:d[2]=0
        if ans!=-1:ans=d[1]*10+d[2]
    else:
        if d[1]==-1:d[1]=0
        if ans!=-1:ans=d[1]
print(ans)