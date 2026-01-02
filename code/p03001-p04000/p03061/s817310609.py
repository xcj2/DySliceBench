class SegmentTree:
    def __init__(self, seq, func="min"):
        if func=="min":
            self.f = min
            self.e = float('inf')
        if func=="max":
            self.f = max
            self.e = -float('inf')
        if func=="gcd":
            self.f = gcd
            self.e = 0
        self._n = len(seq)
        self.n_seg = 2**(self._n-1).bit_length()
        self.seg = [self.e]*2*self.n_seg
        
        for i in range(self._n):
            self.seg[self.n_seg+i-1] = seq[i]
            
        for i in range(self.n_seg-2, -1, -1):
            self.seg[i] = self.f(self.seg[2*i+1], self.seg[2*i+2])
        
    def update(k, val):
        k += self.n_seg -1
        self.seg[k] = val
        while k+1:
            k = (k-1)//2
            self.seg[k] = self.f(self.seg[k*2+1], self.seg[k*2+2])
        
    def query(self, a, b):
        if b<=a:
            return self.e
        a += self.n_seg-1
        b += self.n_seg-2
        res = self.e
        while b-a>1:
            if a&1==0:
                res = self.f(res, self.seg[a])
            if b&1==1:
                res = self.f(res, self.seg[b])
                b -= 1
            a = a//2
            b = (b-1)//2
        if a==b:
            res = self.f(res, self.seg[a])
        else:
            res = self.f(self.f(res, self.seg[a]), self.seg[b])
        return res
    
    def __repr__(self):
        ret = str(self.seg[self._n-1:])
        return ret

def gcd(a, b):
    if b>a:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a

if __name__=="__main__":
    N = int(input())
    A = list(map(int, input().split()))
    A_seg = SegmentTree(A, func="gcd")
    ans = -1
    for i in range(N):
        ans = max(ans, gcd(A_seg.query(0, i), A_seg.query(i+1, N)))
    print(ans)