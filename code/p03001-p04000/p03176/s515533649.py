class SegmentTree:  # 0-indexed
    def __init__(self, array, operation=min, identity=10**30):
        self.identity = identity
        self.n = len(array)
        self.N = 1 << (self.n - 1).bit_length()
        self.tree = [self.identity] * 2 * self.N
        self.opr = operation
        for i in range(self.n):
            self.tree[i+self.N-1] = array[i]
        for i in range(self.N-2, -1, -1):
            self.tree[i] = self.opr(self.tree[2*i+1], self.tree[2*i+2])

    def value(self, k):
        return self.tree[k+self.N-1]

    def update(self, k, x):
        k += self.N-1
        self.tree[k] = x
        while k+1:
            k = (k-1)//2
            self.tree[k] = self.opr(self.tree[k*2+1], self.tree[k*2+2])

    def query(self, p, q):  # [p,q)
        if q <= p:
            print("Oops!  That was no valid number.  Try again...")
            exit()
        p += self.N-1
        q += self.N-2
        res = self.identity
        while q-p > 1:
            if p & 1 == 0:
                res = self.opr(res, self.tree[p])
            if q & 1 == 1:
                res = self.opr(res, self.tree[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = self.opr(res, self.tree[p])
        else:
            res = self.opr(self.opr(res, self.tree[p]), self.tree[q])
        return res


n = int(input())
h = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

dp = [0 for _ in range(n+1)]

ST = SegmentTree(dp, max, -1)

for i in range(n):
    ST.update(h[i], a[i] + ST.query(0, h[i]))

print(ST.query(0, n+1))
