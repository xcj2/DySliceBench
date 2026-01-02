#####segfunc######
class SegTree:
    def segfunc(self, x, y):
        return max(x,y)

    def __init__(self, init_val):
        #set_val
        #####単位元######
        self.ide_ele = 0
        n = len(init_val)
        #num:n以上の最小の2のべき乗
        self.num =2**(n-1).bit_length()
        self.seg=[self.ide_ele]*2*self.num
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]    
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1],self.seg[k*2+2])
    def query(self, p, q):
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



N = int(input())

S = list(input())
ALPHAS = [[0] * (N+1) for i in range(26)]
alpha2num = lambda c: ord(c) - ord('a')
for i in range(N):
    ALPHAS[alpha2num(S[i])][i] = 1
for i,alpha in enumerate(ALPHAS):
    ALPHAS[i] = SegTree(alpha)
ALPHAS = tuple(ALPHAS)
Q = int(input())
for _ in range(Q):
    q,a,b = map(lambda c:c,input().split())
    if q == '2':
        l = int(a)-1
        r = int(b)
        ans = 0
        for i in range(26):
            ans += ALPHAS[i].query(l,r)
        print(ans)
    if q == '1':
        i = int(a)-1
        p_s = S[i]
        s = b
        S[i] = s
        ALPHAS[alpha2num(p_s)].update(i,0)
        ALPHAS[alpha2num(s)].update(i,1)