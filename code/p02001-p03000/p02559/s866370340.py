def segfunc(x,y):
    return x+y

class SegmentTree():
    def __init__(self,A,n,ide_ele):
        self.ide_ele=ide_ele
        self.num =2**(n-1).bit_length()
        self.seg = [self.ide_ele]*2*self.num
        #set_val
        for i in range(n):
            self.seg[i+self.num-1]=A[i]
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=segfunc(self.seg[2*i+1],self.seg[2*i+2])

    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = segfunc(self.seg[k*2+1],self.seg[k*2+2])

    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = segfunc(res,self.seg[p])
            if q&1 == 1:
                res = segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc(res,self.seg[p])
        else:
            res = segfunc(segfunc(res,self.seg[p]),self.seg[q])
        return res
N,Q = list(map(int,input().split()))
A = list(map(int,input().split()))
ST = SegmentTree(A,N,0)
for i in range(Q):
    n,p,x = list(map(int,input().split()))
    if n==1:
        print(ST.query(p,x))
    else:
        A[p] += x
        ST.update(p,A[p])
