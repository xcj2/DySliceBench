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
    inf=10**7
    n,k=map(int,input().split())
    P=list(map(int,input().split()))
    segmax=SegmentTree(P,0,max)
    segmin=SegmentTree(P,inf,min)
    ans=n-k+1
    for i in range(n-k):
        if segmin.query(i,i+k)==P[i] and segmax.query(i,i+k)<P[i+k]:
            ans-=1
    tmp=1
    cnt=0
    for i in range(n-1):
        if P[i]>P[i+1]:
            if tmp>=k:
                cnt+=1
            tmp=1
        else:
            tmp+=1
    if tmp>=k:
        cnt+=1
    if cnt:
        ans-=cnt-1
    print(ans)
    
if __name__=='__main__':
    main()