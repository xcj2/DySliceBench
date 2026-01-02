from bisect import bisect_right
import sys
input = sys.stdin.buffer.readline

class SegmentTree:
    """
    0-indexed
    query : [L, R)
    """
    def __init__(self, size, initValue, cmpFunc):
        self.size = 1 << (size.bit_length())  # 完全二分木にする
        self.data = [initValue] * (2 * self.size - 1)
        self.initValue = initValue
        self.cmpFunc = cmpFunc

    def build(self, rawData):
        self.data[self.size - 1: self.size - 1 + len(rawData)] = rawData
        for i in range(self.size - 1)[:: -1]:
            self.data[i] = self.cmpFunc(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, index, value):
        index += self.size - 1
        self.data[index] = value
        while index >= 0:
            index = (index - 1) // 2
            self.data[index] = self.cmpFunc(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):
        L = left + self.size
        R = right + self.size
        ret = self.initValue
        while L < R:
            if R & 1:
                R -= 1
                ret = self.cmpFunc(ret, self.data[R - 1])
            if L & 1:
                ret = self.cmpFunc(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret

N, D, A = map(int, input().split())
XH = [tuple(map(int, input().split())) for _ in range(N)]
XH.sort()
X = [x for x, _ in XH]

tree = SegmentTree(N + 1, 0, lambda a, b: a + b)

ans = 0
for i, (x, h) in enumerate(XH):
    cnt = tree.query(0, i + 1)
    h -= cnt * A

    if h <= 0:
        continue

    ness = -(-h // A)
    ans += ness
    tree.update(i, tree.query(i, i + 1) + ness)
    j = bisect_right(X, x + 2 * D)
    tree.update(j, tree.query(j, j + 1) - ness)

print(ans)