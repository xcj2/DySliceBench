class SegTree:
    """
    内部実装1-indexed．
    set_valやfoldには0-indexedでアクセス．
    2べきに直さなくてよい．
    Range Minimum Query．
    X_unit 大きい数 X_f min
    """
    X_unit = 2147483647  # (1 << 31) - 1
    X_f = min

    def __init__(self, N):
        self.N = N
        self.X = [self.X_unit] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_unit
        vR = self.X_unit
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


def main():
    N, Q = (int(i) for i in input().split())
    seg = SegTree(N)
    for _ in range(Q):
        com, x, y = (int(i) for i in input().split())
        if com == 0:
            seg.set_val(x, y)
        else:
            print(seg.fold(x, y+1))


if __name__ == '__main__':
    main()

