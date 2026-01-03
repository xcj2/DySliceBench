from bisect import*
class SquareSkipList:
    def __init__(self,values=[],square=1000,seed=42):
        INF=10**18
        self.square=square
        self.layer1=layer1=[]
        self.layer0=layer0=[]
        y=seed
        l0=[]
        for v in values:
            y^=(y&0x7ffff)<<13
            y^=y>>17
            y^=(y&0x7ffffff)<<5
            if y%square<1:
                layer0+=l0,
                l0=[]
                layer1+=v,
            else:l0+=v,
        layer1+=INF,
        layer0+=l0,
        self.rand_y=y
    def add(self,x):
        y=self.rand_y
        y^=(y&0x7ffff)<<13
        y^=y>>17
        y^=(y&0x7ffffff)<<5
        self.rand_y=y
        if y%self.square<1:
            layer1,layer0=self.layer1,self.layer0
            idx1=bisect(layer1,x)
            layer1.insert(idx1,x)
            layer0_idx1=layer0[idx1]
            idx0=bisect(layer0_idx1,x)
            layer0.insert(idx1+1,layer0_idx1[idx0:])
            del layer0_idx1[idx0:]
        else:
            idx1=bisect(self.layer1,x)
            insort(self.layer0[idx1],x)
    def remove(self,x):
        layer1,layer0=self.layer1,self.layer0
        idx1=bisect_left(layer1,x)
        layer0_idx1=layer0[idx1]
        idx0=bisect_left(layer0_idx1,x)
        if idx0==len(layer0_idx1):
            del layer1[idx1]
            layer0[idx1]+=layer0.pop(idx1+1)
        else:del layer0_idx1[idx0]
    def search_higher(self,x):
        layer1,layer0=self.layer1,self.layer0
        idx1=bisect(layer1,x)
        layer0_idx1=layer0[idx1]
        idx0=bisect(layer0_idx1,x)
        return layer1[idx1]if idx0==len(layer0_idx1)else layer0_idx1[idx0]
    def search_lower(self,x):
        layer1,layer0=self.layer1,self.layer0
        idx1=bisect_left(layer1,x)
        layer0_idx1=layer0[idx1]
        idx0=bisect_left(layer0_idx1,x)
        return layer1[idx1-1]if idx0<1else layer0_idx1[idx0-1]
    def pop(self,idx):
        layer1,layer0=self.layer1,self.layer0
        s=-1
        for i,l0 in enumerate(layer0):
            s+=len(l0)+1
            if s>=idx:break
        if s==idx:
            layer0[i]+=layer0[i+1]
            del layer0[i+1]
            return layer1.pop(i)
        else:return layer0[i].pop(idx-s)
def main():
    n,*a=map(int,open(0).read().split())
    l=[0]*n
    for i,v in enumerate(a,1):l[v-1]=i
    t=SquareSkipList([])
    t.add(0)
    t.add(n+1)
    c=0
    for i,v in enumerate(l,1):
        c+=(t.search_higher(v)-v)*(v-t.search_lower(v))*i
        t.add(v)
    print(c)
main()