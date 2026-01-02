import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

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
        return self.A[i+self.leaf-1]
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
    def query(self,a,b):
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
            l>>=1
            r>>=1
        return res

def f(a,b):
    return max(a,b)

n=int(input())
H=list(map(int,input().split()))
A=list(map(int,input().split()))
seg=SegmentTree(n+1,0,f)
for h,a in zip(H,A):
    t=seg.query(0,h)
    seg.update(h,a+t)
print(seg.get_top())