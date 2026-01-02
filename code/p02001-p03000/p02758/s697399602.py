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
    
### 使い方 ##

import sys
input = sys.stdin.readline
N = int(input())


GOTO = [i for i in range(1,N+1)]
INF = 10**15
ide_ele = -1
SEG = SegTree(GOTO,ide_ele,max)


LIST = []
XX = []
mod = 998244353

for i in range(N):
    X,D = map(int,input().split())
    LIST.append([X,D])

LIST.sort(key=lambda x: x[0])
for i in range(N):
    XX.append(LIST[i][0])

#print(LIST)
import bisect
for i in range(N-1):
    j = N-2-i
    Xj = LIST[j][0]
    Dj = LIST[j][1]
    Nj = bisect.bisect_right(XX, Xj+Dj-1)
    #print(Xj,Dj,j+1,Nj)
    NEXT = SEG.query(j+1,Nj)
    if NEXT != -1:
        GOTO[j] = NEXT
        SEG.update(j,NEXT)
    
S = [-1]*(N+1)
S[N] = 1

#print(LIST)
#print(GOTO)
for i in range(N):
    j = N-1-i
    S[j] = S[j+1] + S[GOTO[j]]
    S[j] %= mod

print(S[0])