import sys


class AlgSegmentTreeMin:
    def __init__(self, n, default_value):
        self.Nelem = n
        self.default_value = default_value
        self.size = 1 << (n.bit_length())
        self.data = [default_value] * (2 * self.size)

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
    input = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, m = list(map(int, input().split()))
    stree = AlgSegmentTreeMin(n, 10 ** 15)
    lrc = [list(map(int, input().split())) for _ in range(m)]
    lrc.sort()
    stree.update(0, 0)
    for l, r, c in lrc:
        l -= 1
        r -= 1
        tm = stree.get_value(l, r)
        now = stree.get_value(r, r)
        tm = tm + c if tm + c < now else now
        stree.update(r, tm)
    mt = stree.get_value(n-1, n)
    print(mt if mt != stree.default_value else -1)


if __name__ == '__main__':
    solve()
