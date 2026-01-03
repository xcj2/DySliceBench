from bisect import bisect_left
class SEGTree:
    def __init__(self,n):
        self.Unit=0
        i=1
        while(i<n):
            i*=2
        self.SEG=[self.Unit]*(2*i-1)
        self.d=i
    def update(self,i,x):
        i+=self.d-1
        self.SEG[i]+=x
        while i>0:
            i=(i-1)//2
            self.SEG[i]=self.SEG[i*2+1]+self.SEG[i*2+2]
    def find(self,a,b,k,l,r):
        if r<=a or b<=l:
            return self.Unit
        if a<=l and r<=b:
            return self.SEG[k]
        else:
            c1=self.find(a,b,2*k+1,l,(l+r)//2)
            c2=self.find(a,b,2*k+2,(l+r)//2,r)
            return c1+c2
    def get(self,a,b):
        return self.find(a,b,0,0,self.d)
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
seg=SEGTree(N+1)
ans=0
for i in range(N+1):
    ans+=seg.get(0,dic[B[i]]+1)
    seg.update(dic[B[i]],1)
print(ans)