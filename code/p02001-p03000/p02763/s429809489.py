class SegTree:
    def __init__(self, init_val, ide_ele, segfunc):
        self.n = len(init_val)
        self.num =2**(self.n-1).bit_length()
        self.ide_ele = ide_ele
        self.seg = [self.ide_ele]*2*self.num
        self.segfunc = segfunc
        
        #set_val
        for i in range(self.n):
            self.seg[i+self.num-1] = init_val[i]    
        #built
        for i in range(self.num-2,-1,-1) :
            self.seg[i] = segfunc(self.seg[2*i+1], self.seg[2*i+2]) 
    
    def update(self, k, x):
        k += self.num-1
        self.seg[k] = x
        while k+1:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[k*2+1], self.seg[k*2+2])
    
    def query(self, p, q):
        if q<=p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q-p>1:
            if p&1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q&1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res
    
import sys
input = sys.stdin.readline
N = int(input())
S = input()
L = [-1]*N
for i in range(N):
    L[i] = 2**(ord(S[i]) - ord('a'))
    
def segfunc(a,b):
    return a | b

Seg = SegTree(L,0,segfunc)

Q = int(input())

for _ in range(Q):
    q,a,b = input().split()
    if q == '1':
        i = int(a)-1
        c = 2**(ord(b) - ord('a'))
        Seg.update(i,c)
    elif q=='2':
        l = int(a)-1
        r = int(b)-1
        X = Seg.query(l,r+1)
        tmp = 0
        for j in range(30):
            if X%2==1:
                tmp += 1
            X//=2
        print(tmp)