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
C=sorted(set(B))
t=len(C)
D={ C[i]:i for i in range(t)}
tree=BIT(t)
ans=0
for i in range(N+1):
    ans+=tree.search(D[B[i]]+1)
    tree.add(D[B[i]]+1,1)
print(ans)