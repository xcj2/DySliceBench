#from fractions import gcd
"""
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
"""
def gcd(a,b):
    if b==0:
        return a
    r=a%b
    while r!=0:
        a=b
        b=r
        r=a%b
    return b
class SegTree():
    def __init__(self, lists, function, basement):
        self.n = len(lists)
        self.K = (self.n-1).bit_length()
        self.func = function
        self.basement = basement
        self.seg = [basement]*2**(self.K+1)#basementで初期化
 
        for i in range(self.n):
            self.seg[i+2**self.K-1] = lists[i]
 
        for i in range(2**(self.K)-2, -1, -1):
            self.seg[i] = self.func(self.seg[2*i+1], self.seg[2*i+2])
 
    def update(self, k, value):
        # 0-indexでa[k]の値をvalueに変更
        k += 2**self.K-1
        self.seg[k] = value
        while k:
            k = (k-1)//2
            self.seg[k] = self.func(self.seg[k*2+1], self.seg[k*2+2])
 
    def query(self, p, q):
        # 0-indexで[p,q)の値を取得する
        if q <= p:
            return self.basement
        num = 2**self.K
        p += num-1
        q += num-2
        res = self.basement
        while q-p > 1:
            if p & 1 == 0:
                res = self.func(res, self.seg[p])
            if q & 1 == 1:
                res = self.func(res, self.seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.func(res, self.seg[p])
        else:
            res = self.func(self.func(res, self.seg[p]), self.seg[q])
        return res
 

n=int(input())
a=list(map(int,input().split()))
seg=SegTree(a,gcd,0)
ans=1
for i in range(n):
    ans=max(ans,gcd(seg.query(0,i),seg.query(i+1,n)))
print(ans)
