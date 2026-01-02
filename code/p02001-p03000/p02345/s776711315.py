
class SegmentTree:
    def __init__(self, n, f, gen):
        self.n = n
        self.size = 1
        self.gen = gen
        self.f = f
        while self.size < n:
            self.size *= 2
        self.seg = [gen] * (2 * self.size)

    def set(k, x):
        self.seg[k + self.size] = x

    def build(self):
        k = self.size - 1
        while k>0:
            self.seg[k] = self.f(self.seg[2 * k], self.seg[2 * k + 1])
            k -= 1

    def update(self, i, x):
        k = i + self.size
        self.seg[k] = x
        while k > 0:
            k >>= 1
            self.seg[k] = self.f(self.seg[2 * k], self.seg[2 * k + 1])
    
    def query(self, a, b):
        """
        [a,b)
        """
        L = self.gen
        R = self.gen
        A = a + self.size
        B = b + self.size
        while A<B:
            if A%2:
                L = self.f(L, self.seg[A])
                A += 1
            if B%2:
                B -= 1
                R = self.f(self.seg[B], R)
            A >>= 1
            B >>= 1
        return f(L, R)
    


def f(a, b):
    return min(a,b)

def main():
    n, q = map(int, input().split())
    seg = SegmentTree(n, f, 2**31-1)
    seg.build()

    for _ in range(q):
        t, x, y = map(int, input().split())
        if t==0:
            seg.update(x, y)
        else:
            print(seg.query(x, y+1))


if __name__ == "__main__":
    main()    


