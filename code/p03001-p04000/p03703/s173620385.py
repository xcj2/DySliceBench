from bisect import bisect_left
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

N,K=map(int,input().split())
a=[int(input()) for i in range(N)]
cum=[0]*(N+1)
for i in range(N):
    cum[i+1]=cum[i]+a[i]
B=[cum[i]-i*K for i in range(N+1)]

dic={}
li=sorted(B)
for i in range(N+1):
    dic[B[i]]=bisect_left(li,B[i])
bit=BIT(N+1)
ans=0
for i in range(N+1):
    ans+=bit.get(dic[B[i]]+1)
    bit.add(dic[B[i]],1)
print(ans)
