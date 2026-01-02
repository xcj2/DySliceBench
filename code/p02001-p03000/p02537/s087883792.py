"""
import sys
input = sys.stdin.readline

def main():
    



    
if __name__ == "__main__":
    main()

"""

import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, func, e, arrange=None):
        self.init(n)
        self.func = func
        self.e = e
        self.make_arrange(arrange)
    
    def init(self, n):
        self.inf = pow(2, 32)
        self.n = n
        self.N = 1
        while self.N < self.n:
            self.N *= 2
        self.size = self.N * 2
    
    def make_arrange(self, arrange):
        self.set_arrange(arrange)
        self.construct(arrange)

    def set_arrange(self, arrange):
        if arrange == None:
            self.segment = [self.e]*(self.size)
            return
        self.segment = [0]*(self.N) + arrange + [self.e]*(self.size-self.N-self.n)
    
    def construct(self, arrange):
        if arrange == None:
            return
        for i in range(self.N-1, 0, -1):
            self.segment[i] = self.func(self.segment[2*i], self.segment[2*i+1])
    
    def update(self, i, x):
        i += (self.N - 1)
        self.segment[i] = x
        while i > 1:
            i = i//2
            self.segment[i] = self.func(self.segment[2*i], self.segment[2*i+1])
    

    def count(self, l, r):
        res = self.e
        l += self.N-1
        r += self.N
        while r > l:
            if l & 1:
                res = self.func(res, self.segment[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.segment[r])
            l >>= 1
            r >>= 1
        return res
    
    """
    二分探索
    これは区間[l, r]にてx以上となる最小のインデックスを返すメソッド
    まずfind_l：二分木左側を探索し、そこに条件を満たすものがなかったらfind_：右側を探索
    インデックスの最大最小により左右を使い分ける
    """

    def bisect_sub(self, a, b, k, l, r, x):
        if r <= a or b <= l:
            return b+1
        if self.segment[k] < x:
            return b+1
        if k >= self.N:
            return r
        
        find_l = self.bisect_sub(a, b, 2*k, l, (l+r)//2, x)
        if find_l <= b:
            return find_l

        find_r = self.bisect_sub(a, b, 2*k+1, (l+r)//2, r, x)
        return find_r

    def bisect(self, l, r, x):
        return self.bisect_sub(l-1, r, 1, 0, self.size-self.N, x)

mod = 998244353

def main():
    n, k = map(int, input().split())
    a = [None]*n
    sub = 1
    e = 0
    func = max
    ma = 300001
    seg = SegmentTree(ma, func, e)
    ans = 0
    for i in range(n):
        a = int(input())
        sub = seg.count(max(0, a-k), min(a+k, ma)) + 1
        ans = max(ans, sub)
        seg.update(a, sub)
    
    print(ans)

main()
