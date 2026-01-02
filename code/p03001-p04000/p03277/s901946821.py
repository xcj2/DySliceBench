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
N=int(input())
A=[int(i) for i in input().split()]
if ((N*(N+1))//2)%2==1:
    a=((N*(N+1))//2)//2+1
else:
    a=((N*(N+1))//2)//2
#a=((N*(N+1))//2)-((N*(N+1))//2)//2-1
def f(s):#ans is ijou s
    X=[1 if a>=s else -1 for a in A]
    p=[0]*(N+1)
    ma=0
    mi=0
    for i in range(1,N+1):
        p[i]=p[i-1]+X[i-1]
        ma=max(p[i],ma)
        mi=min(p[i],mi)
    tree=BIT(ma-mi+1)
    num=0
    for i in range(1,N+2):
        num+=tree.search(p[i-1]-mi+1)
        tree.add(p[i-1]-mi+1,1)
    if num>=a:
        return True
    else:
        return False
x=10**9+1
y=-1
while x-y>1:
    mid=(x+y)//2
    if f(mid):
        y=mid
    else:
        x=mid
print(y)
