import sys

inf = (1 << 31) - 1

def solve():
    n, q = map(int, sys.stdin.readline().split())

    bit = BinaryIndexedTree([0]*n)

    for qi in range(q):
        c, x, y = map(int, sys.stdin.readline().split())

        if c == 0:
            x -= 1
            bit.add(x, y)
        else:
            ans = bit.get_sum(y) - bit.get_sum(x - 1)
            print(ans)

class BinaryIndexedTree:
    def __init__(self, a):
        self.n = len(a)
        self.bit = [0]*(self.n + 1)

        for i in range(1, self.n + 1):
            self.bit[i] += a[i - 1]

            if i + (i & (-i)) <= self.n:
                self.bit[i + (i & (-i))] += self.bit[i]

    def add(self, i, x):
        i += 1

        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)

    def get_sum(self, r):
        res = 0

        while r > 0:
            res += self.bit[r]
            r -= r & (-r)

        return res

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