def func(x,y):
    return  x if x < y else y

class SegmentTree:
    def __init__(self, n): #a1, a2, ..., an
        n_ = 1
        while n_ < n:
            n_ *= 2

        self.n = n_
        self.arr = [2**31-1] * (2*self.n-1)

    def update(self, k, a): #0_indexed
        k += self.n - 1
        self.arr[k] = a

        while k > 0:
            k = (k-1) // 2
            self.arr[k] = func(self.arr[2*k+1], self.arr[2*k+2])

    def query(self, l, r):#[l,r)の値を返す
        L, R = l+self.n, r+self.n
        ide_ele = 2**31-1
         #ex) 最小値のセグ木 → +inf
         #　和のセグ木 → 0
         #　積のセグ木 → 1
         #  gcdのセグ木 → 0
        res = ide_ele
        while L < R:
            if R & 1:
                R -= 1
                res = func(res, self.arr[R-1])

            if L & 1:
                res = func(res, self.arr[L-1])
                L += 1

            L >>= 1
            R >>= 1

        return res
#0-indexedな気がする
n,q=map(int,input().split())
sg=SegmentTree(n)
for _ in range(q):
    c,x,y=map(int,input().split())
    if c==0:
        sg.update(x,y)
    else:
        print(sg.query(x,y+1))

