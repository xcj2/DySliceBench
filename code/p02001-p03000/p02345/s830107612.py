import sys

inf = (1 << 31) - 1

def solve():
    n, q = map(int, sys.stdin.readline().split())

    a = [inf] * n
    sg = SegTree(a)

    for qi in range(q):
        c, x, y = map(int, sys.stdin.readline().split())

        if c == 0:
            sg.update(x, y)
        else:
            ans = sg.find(x, y + 1, 0, 0, 2**sg.depth)

            print(ans)


class SegTree:

    def __init__(self, a):
        self.n = len(a)
        self.depth = 0

        while 2**self.depth < self.n:
            self.depth += 1

        self.dat = [inf] * (2**(self.depth + 1) - 1)

        self.dat[2**self.depth - 1:2**self.depth - 1 + self.n] = a[:]

        for i in range(2**self.depth - 2, -1, -1):
            self.dat[i] = min(self.dat[2*i + 1], self.dat[2*i + 1])

    def update(self, i, x):
        i += 2**self.depth - 1
        self.dat[i] = x

        while i > 0:
            i = (i - 1) // 2
            self.dat[i] = min(self.dat[2*i + 1], self.dat[2*i + 2])

        return

    def find(self, s, t, k, left, right):
        if t <= left or right <= s:
            return inf
        if s <= left and right <= t:
            return self.dat[k]

        vl = self.find(s, t, 2*k + 1, left, (left + right) // 2)
        vr = self.find(s, t, 2*k + 2, (left + right) // 2, right)

        return min(vl, vr)

if __name__ == '__main__':
    solve()