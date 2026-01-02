class BIT:
    def __init__(self,N):
        self.N=N
        self.bit=[0]*N
    def add(self,a,w):
        x=a
        while(x<self.N):
            self.bit[x]+=w
            x|=x+1
    def get(self,a):
        ret,x=0,a-1
        while(x>=0):
            ret+=self.bit[x]
            x=(x&(x+1))-1
        return ret
    def cum(self,l,r):
        return self.get(r)-self.get(l) 

def check(k):
    li=[]
    for i in range(N):
        li.append(1 if A[i]<=k else 0)

    c=[0]*(N+1)
    for i in range(N):
        c[i+1]=c[i]+li[i]
        
    d=[]
    for i in range(N+1):
        d.append(2*c[i]-i)
        
    S=sorted(set(d))
    dic={}
    for i,x in enumerate(S):
        dic[x]=i
    
    bit=BIT(N+1)
    res=0
    for i in range(N+1):
        bit.add(dic[d[i]],1)
        res+=bit.get(dic[d[i]])
    
    if res>M:
        return True
    else:
        return False

N=int(input())
A=list(map(int,input().split()))
M=N*(N+1)//4
l,r=-1,max(A)+1
while(r-l>1):
    k=(l+r)//2
    if check(k):
        r=k
    else:
        l=k

print(r)