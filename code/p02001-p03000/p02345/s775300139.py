class SqrtDecomposition():
    def __init__(self, array, f):
        self.dat = array
        self.f = f
        m = int(pow(len(array), 0.5))
        if m**2 < len(array):
            m += 1
        self.m = m
        self.dat2 = []
        for i in range(m):
            if i * m >= len(array):
                break
            self.dat2 += [f(self.dat[m * i:m * (i + 1)])]

    def update(self, a, x):
        m = self.m
        dat = self.dat
        dat2 = self.dat2
        f = self.f
        dat[a] = x
        a2 = a // m
        al = m * a2
        ar = al + m
        dat2[a2] = f(dat[al:ar])

    def query(self, a, b):
        dat = self.dat
        dat2 = self.dat2
        f = self.f
        m = self.m
        a2 = a // m
        ar = a2 * m + m
        b2 = b // m
        bl = b2 * m
        if ar > bl:
            return f(dat[a:b])
        else:
            return f(dat[a:ar] + dat2[a2 + 1:b2] + dat[bl:b])


N, Q = [int(_) for _ in input().split()]
Query = [[int(_) for _ in input().split()] for _ in range(Q)]
SD = SqrtDecomposition(array=[2**31 - 1] * N, f=min)
for query in Query:
    if query[0]:
        query[2] += 1
        print(SD.query(*query[1:]))
    else:
        SD.update(*query[1:])

