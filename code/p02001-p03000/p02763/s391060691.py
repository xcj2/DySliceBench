n = int(input())
s = input()
q = int(input())


class SegmentTree:
    def __init__(self, a, func=max, one=-10 ** 18):
        self.logn = (len(a) - 1).bit_length()
        self.n = 1 << self.logn
        self.func = func
        self.one = one

        self.b = [self.one] * (2 * self.n - 1)
        for i, j in enumerate(a):
            self.b[i + self.n - 1] = j
        for i in reversed(range(self.n - 1)):
            self.b[i] = self.func(self.b[i * 2 + 1], self.b[i * 2 + 2])

        self.ll = []
        self.rr = []
        i = self.n
        for _ in range(self.logn+1):
            for j in range(0, self.n, i):
                self.ll.append(j)
                self.rr.append(j + i)
            i //= 2

    def get_item(self, i):
        return self.b[i + self.n - 1]

    def update(self, index, x):
        i = index + self.n - 1
        self.b[i] = x
        while i != 0:
            i = (i - 1) // 2
            self.b[i] = self.func(self.b[i * 2 + 1], self.b[i * 2 + 2])

    def update_func(self, index, x):
        i = index + self.n - 1
        self.b[i] = self.func(self.b[i], x)
        while i != 0:
            i = (i - 1) // 2
            self.b[i] = self.func(self.b[i * 2 + 1], self.b[i * 2 + 2])

    def get_segment(self, l, r, i=0):
        ll = self.ll[i]
        rr = self.rr[i]
        if l <= ll and rr <= r:
            return self.b[i]
        elif rr <= l or r <= ll:
            return self.one
        else:
            return self.func(self.get_segment(l, r, i * 2 + 1),
                             self.get_segment(l, r, i * 2 + 2))


def get_int(s):
    abc = "abcdefghijklmnopqrstuvwxyz"
    return 1 << abc.index(s)


seg = SegmentTree([get_int(i) for i in s], int.__or__, 0)

for _ in range(q):
    q, i, j = input().split()
    if q == "1":
        seg.update(int(i) - 1, get_int(j))
    else:
        aa = seg.get_segment(int(i) - 1, int(j))
        ans = 0
        for i in range(26):
            if (aa >> i) & 1 == 1:
                ans += 1
        print(ans)
