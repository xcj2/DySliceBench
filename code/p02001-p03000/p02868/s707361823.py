import sys


class AlgSegmentTreeMin:
    def __init__(self, n, default_value):
        self.Nelem = n
        self.default_value = default_value
        self.size = 1 << (n.bit_length())
        self.data = [default_value] * (2 * self.size)

    def build(self, raw_data):
        for i, x in enumerate(raw_data):
            self.data[self.size + i] = x
        for i in range(self.size - 1, 0, -1):
            x = self.data[i + i]
            y = self.data[i + i + 1]
            self.data[i] = min(x, y)

    def update(self, i, x):
        i += self.size
        self.data[i] = x
        i >>= 1
        while i:
            x = self.data[i + i]
            y = self.data[i + i + 1]
            self.data[i] = min(x, y)
            i >>= 1

    def get_value(self, left, right):
        left += self.size
        right += self.size + 1
        x = self.default_value
        while left < right:
            if left & 1:
                y = self.data[left]
                x = min(x, y)
                left += 1
            if right & 1:
                right -= 1
                y = self.data[right]
                x = min(x, y)
            left >>= 1
            right >>= 1
        return x


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().rstrip('\n').split()))
    stree = AlgSegmentTreeMin(n, 10 ** 15)
    stree.update(0, 0)
    lrc = [list(map(int, input().rstrip('\n').split())) for _ in range(m)]
    lrc.sort()
    for l, r, c in lrc:
        l -= 1
        r -= 1
        tm = stree.get_value(l, r)
        stree.update(r, min(tm + c, stree.get_value(r, r + 1)))
    mt = stree.get_value(n-1, n)
    print(mt if mt != stree.default_value else -1)


if __name__ == '__main__':
    solve()
