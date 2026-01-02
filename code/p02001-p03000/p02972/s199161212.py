import sys
sys.setrecursionlimit(10**6)
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]

n=I()
a=[0]+LI()
b=[0]*(n+1)
c=[0]*(n+1)
for i in range(n,0,-1):
    if c[i]!=a[i]:
        b[i]=1 #-b[i]
        c[i]=1-c[i]
        for j in range(2,int(i**0.5+1)):
            if i%j==0:
                c[j]=1-c[j]
                if j!=i//j: c[i//j]=1-c[i//j]
                #print('i=',i,'change',j,i//j)

s=sum(b)
if s%2!=a[1]:
    b[1]=1-b[1]
s=sum(b)    
print(s)

ans=[]
for i in range(1,n+1):
    if b[i]==1:
        #print(i,end=' ')
        ans.append(i)
if s!=0:
    print(*ans)
