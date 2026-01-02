from math import ceil,sqrt,log,gcd
def ii():return int(input())
def si():return input()
def mi():return map(int,input().split())
def li():return list(mi())


    

n,m,x=mi()

a=[[0 for i in range(m)]for j in range(n)]
p=[0]*n
for i in range(n):
    a1=li()
    p[i]=a1[0]
    a[i]=a1[1:]

ans=1000000007
for i in range(1,pow(2,n)):
    s=bin(i)[2:]
    s='0'*(n-len(s))+s
    s1=0
    x1=[0]*m
    for j in range(n):
        if s[j]=='1':
            for k in range(m):
                x1[k]+=a[j][k]
            s1+=p[j] 
    f1=1
    for j in range(m):
        if(x1[j]<x):
            f1=0
        
    if(f1):
        ans=min(ans,s1)
if(ans==1000000007):
    ans=-1
print(ans)