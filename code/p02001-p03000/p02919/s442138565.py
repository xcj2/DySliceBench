n = int(input())
xs = list(map(int, input().split()))
x2i = {}
for i, x in enumerate(xs):
    x2i[x] = i+1
ll = [0] * (n+2)
rr = [n+1] * (n+2)

def find_l(l, r, default):
    m, m2 = 0, 0
    mi=mi2=default
    for i in range(r-l):
        i = i + l
        if ll[i] > m:
            mi, m = i, ll[i]
    for i in range(r-l):
        i = i + l
        if i == mi:
            continue
        if ll[i] > m2:
            mi2, m2 = i, ll[i]
    return max(mi, mi2), min(mi, mi2)

def find_r(l, r, default):
    m, m2 = n+1, n+1
    mi=mi2=default
    for i in range(r-l):
        i = i + l
        if rr[i] < m:
            mi, m = i, rr[i]
    for i in range(r-l):
        i = i + l
        if i == mi:
            continue
        if rr[i] < m2:
            mi2, m2 = i, rr[i]
    return max(mi, mi2), min(mi, mi2)

class ss_min:

    def __init__(self, init_val, n, ide_ele):
        self.segfunc = min
        self.num = 2**(n-1).bit_length()
        self.ide_ele = ide_ele
        self.seg=[self.ide_ele]*2*self.num
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]    
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k+1:
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
class ss_max:

    def __init__(self, init_val, n, ide_ele):
        self.segfunc = max
        self.num = 2**(n-1).bit_length()
        self.ide_ele = ide_ele
        self.seg=[self.ide_ele]*2*self.num
        for i in range(n):
            self.seg[i+self.num-1]=init_val[i]    
        for i in range(self.num-2,-1,-1) :
            self.seg[i]=self.segfunc(self.seg[2*i+1],self.seg[2*i+2]) 
        
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k+1:
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

ssmm = ss_min(rr, n+2, n+1)
ssmm2 = ss_max(ll, n+2, 0)

r = 0
for x in range(n):
    x = n - x
#    lmi, lmi2 = find_l(0, x2i[x], 0)

    rmi2 = ssmm.query(x2i[x]+1, n+1)
    ssmm.update(rmi2, n+1)
    rmi = ssmm.query(x2i[x]+1, n+1)
    ssmm.update(rmi2, rmi2)

    lmi = ssmm2.query(0, x2i[x])
    ssmm2.update(lmi, 0)
    lmi2 = ssmm2.query(0, x2i[x])
    ssmm2.update(lmi, lmi)

    a,b,c,d =(x2i[x] - lmi), (lmi - lmi2), (rmi - rmi2), (rmi2 - x2i[x])
    r += (a*c + b*d) * x
#    print(x, r)
#    print(rmi, rmi2, lmi, lmi2)
    ll[x2i[x]] = x2i[x]
    ssmm.update(x2i[x], x2i[x])
    ssmm2.update(x2i[x], x2i[x])
print(r)
