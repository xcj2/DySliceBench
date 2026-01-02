class segtree():
    def segfunc(x,y):
        return min(x,y)
    #####単位元######
    ide_ele = -1
    n=1
    init_val=[0]*n
    #num:n以上の最小の2のべき乗
    num =2**(n-1).bit_length()
    seg=[ide_ele]*2*num
    
    def __init__(self,INIT_VAL,SEGFUNC,IDE_ELE):
        self.ide_ele=IDE_ELE
        self.init_val=[i for i in INIT_VAL]
        self.segfunc=SEGFUNC
        self.n=len(self.init_val)
        self.num =2**(self.n-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num
 
        #set_val
        for i in range(self.n):
            self.seg[i+self.num-1]=self.init_val[i]    
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k+1:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
        
    def query(self,p,q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res=self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res

N,K=map(int,input().split())
A=[int(input()) for i in range(N)]
def solve1(A,K):
    INF=10**15
    MAX_A=300000
    G=segtree([0 for i in range(MAX_A+1)],max,-INF)
    dp=[0 for i in range(N)]
    dp[0]=1
    G.update(A[0],1)
    for i in range(1,N):
        #print([G.query(i,i+1) for i in range(12)])
        inf=max(0,A[i]-K)
        sup=min(MAX_A+1,A[i]+K+1)
        dp[i]=G.query(inf,sup)+1
        G.update(A[i],dp[i])
    #print(dp)
    return max(dp)

def solve2(A,K):
    N=len(A)
    dp=[1 for i in range(N)]
    for i in range(1,N):
        for j in range(i):
            if abs(A[j]-A[i])<=K:
                dp[i]=max(dp[i],dp[j]+1)
    #print(dp)
    return max(dp)

print(solve1(A,K))