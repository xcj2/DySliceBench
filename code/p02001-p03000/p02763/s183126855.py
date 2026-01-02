import numpy as np

def count(n):
    return bin(n).count("1")

def merge(x, y):
    return x | y

def update(Seg, k, x):
    k += len(Seg)//2
    Seg[k] = x
    while k > 0:
        k = (k - 1) // 2
        Seg[k] = Seg[k*2+1]|Seg[k*2+2]

d = {c:(1 << (ord(c)-97)) for c in 'abcdefghijklmnopqrstuvwxyz'}

class SegmentTree:
    def __init__(self, A):
        N = len(A)
        n = (N-1).bit_length()
        self.N = 1 << n
        self.Seg = [0 for i in range(2*self.N)]
        #for i in range(N): self.update(i, A[i])
        if True:
            for i in range(N):
                self.Seg[self.N+i-1] = d[A[i]]
            for i in range(0,self.N-2)[::-1]:
                self.Seg[i] = self.Seg[i*2+1] | self.Seg[i*2+2]

    def update(self, k, x):
        i = self.N+k-1
        self.Seg[i] = d[x]
        while i > 0:
            i = (i-1)//2
            self.Seg[i] = self.Seg[i*2+1]|self.Seg[i*2+2]
    def merge(self, x, y):
        return x | y

    def query(self, a, b):
        return self.query_(a, b, 0, 0, self.N)

    def query_(self, a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        if a <= l and r <= b:
            return self.Seg[k]
        vl = self.query_(a, b, 2*k+1, l, (l+r)//2)
        vr = self.query_(a, b, 2*k+2, (l+r)//2, r)
        return merge(vl, vr)

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = input()[:-1]
    Q = int(input())
    Seg = SegmentTree(S)

    for _ in range(Q):
        q, i, c = input().split()
        if q == '1':
            i = int(i)-1
            Seg.update(i, c)
        else:
            l, r = int(i), int(c)
            print(count(Seg.query(l-1, r)))
main()
