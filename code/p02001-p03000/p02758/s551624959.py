import sys
input=sys.stdin.readline
from bisect import bisect_left

class SegmentTree():
    def __init__(self,param,default,func):
        if isinstance(param,list):
            n=len(param)
        else:
            n=param
        self.d=default
        self.leaf=1<<(n-1).bit_length()
        if isinstance(param,list):
            self.tree=[default]*(self.leaf-1)+param+[default]*(self.leaf-n)
            for i in range(self.leaf-2,-1,-1):
                self.tree[i]=func(self.tree[i*2+1],self.tree[i*2+2])
        else:
            self.tree=[default]*(self.leaf*2-1)
        self.f=func
    def find(self,i):
        return self.tree[i+self.leaf-1]
    def update(self,idx,a):
        idx+=self.leaf-1
        self.tree[idx]=a
        while idx:
            idx=(idx-1)>>1
            self.tree[idx]=self.merge(self.tree[idx*2+1],self.tree[idx*2+2])
    def merge(self,a,b):
        return self.f(a,b)
    def get_top(self):
        return self.tree[0]
    def query(self,a,b): #[a,b)
        T=self.tree
        l,r=a+self.leaf-1,b+self.leaf-1
        res=self.d
        while l<r:
            if not l%2:
                res=self.merge(res,T[l])
                l+=1
            if not r%2:
                r-=1
                res=self.merge(res,T[r])
            l>>=1; r>>=1
        return res

def main():
    mod=998244353
    n=int(input())
    XD=[list(map(int,input().split())) for _ in range(n)]
    XD.sort()
    X=[x for x,d in XD]
    seg=SegmentTree(n,-1,max)
    DP=[0]*(n+1)
    DP[-1]=1
    for i in reversed(range(n)):
        x,d=XD[i]
        j=bisect_left(X,x+d)
        r=max(i,seg.query(i+1,j))
        seg.update(i,r)
        DP[i]=(DP[i+1]+DP[r+1])%mod
    print(DP[0])
    
if __name__=='__main__':
    main()