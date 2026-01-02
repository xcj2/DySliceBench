import sys

inf = (1 << 31) - 1

def solve():
    n, q = map(int, sys.stdin.readline().split())

    sg = SegTree(n)

    for qi in range(q):
        c, x, y = map(int, sys.stdin.readline().split())

        if c == 0:
            sg.update(x, y)
        else:
            ans = sg.find(x, y + 1, 0, 0, 2**sg.d)
            print(ans)

        # print(sg.a)

class SegTree:
    def __init__(self, n):
        self.d = 0

        while (2**self.d) < n:
            self.d += 1

        self.a = [inf] * (2**(self.d+1) - 1)

    def update(self, i, x):
        pos = i + 2**self.d - 1
        self.a[pos] = x

        while pos > 0:
            pos = (pos - 1) // 2
            self.a[pos] = min(self.a[2*pos + 1], self.a[2*pos + 2])

        return

    def find(self, s, t, k, l, r):
        if r <= s or t <= l:
            return inf
        if s <= l and r <= t:
            return self.a[k]

        vl = self.find(s, t, 2*k + 1, l, (l + r) // 2)
        vr = self.find(s, t, 2*k + 2, (l + r) // 2, r)

        return min(vl, vr)

if __name__ == '__main__':
    solve()