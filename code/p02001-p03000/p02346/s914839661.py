import sys

inf = (1 << 31) - 1

def solve():
    n, q = map(int, sys.stdin.readline().split())

    sg = SegTree([0]*n)

    for qi in range(q):
        # print(sg.data)
        c, x, y = map(int, sys.stdin.readline().split())

        if c == 0:
            x -= 1
            sg.add(x, y)
        else:
            x, y = x-1, y-1
            ans = sg.get_sum(x, y + 1, 0, 0, 2**sg.depth)
            print(ans)

class SegTree:
    def __init__(self, a):
        self.n = len(a)
        self.depth = 0

        while 2**self.depth < self.n:
            self.depth += 1

        self.data = [0]*(2**(self.depth + 1) - 1)

        self.data[2**(self.depth) - 1:2**(self.depth) - 1 + self.n] = a[:]

        for i in range(2**self.depth - 2, -1, -1):
            self.data[i] = self.data[2*i + 1] + self.data[2*i + 2]

    def add(self, i, x):
        i += 2**self.depth - 1
        self.data[i] += x

        while i > 0:
            i = (i - 1) // 2
            self.data[i] += x

    def get_sum(self, s, t, k, left, right):
        if t <= left or right <= s:
            return 0
        if s <= left and right <= t:
            return self.data[k]

        vl = self.get_sum(s, t, 2*k + 1, left, (left + right) // 2)
        vr = self.get_sum(s, t, 2*k + 2, (left + right) // 2, right)

        return vl + vr

if __name__ == '__main__':
    solve()