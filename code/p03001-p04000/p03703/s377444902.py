from itertools import accumulate
import sys
sys.setrecursionlimit(10**8)
class BIT():
    def __init__(self,number):
        self.n=number
        self.list=[0]*(number+1)
        
    def add(self,i,x):#ith added x  1indexed
        while i<=self.n:
            self.list[i]+=x
            i+=i&-i
            
    def search(self,i):#1-i sum
        s=0
        while i>0:
            s+=self.list[i]
            i-=i&-i
        return s
    
    def suma(self,i,j):#i,i+1,..j sum
        return self.search(j)-self.search(i-1)

N,K=map(int,input().split())
A=[int(input()) for i in range(N)]
B=list(accumulate([0]+A))
for i in range(N+1):
    B[i]-=K*i
C=sorted((B[i],i) for i in range(N+1))
D=[-1]*(N+1)
D[C[0][1]]=0
s=C[0][0]
t=0
for i in range(1,N+1):
    if s<C[i][0]:
        s=C[i][0]
        t+=1
        D[C[i][1]]=t
    else:
        D[C[i][1]]=t
tree=BIT(t+1)
ans=0
for i in range(N+1):
    ans+=tree.search(D[i]+1)
    tree.add(D[i]+1,1)
print(ans)