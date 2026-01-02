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
        for i in rawData(self.size - 1)[:: -1]:
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

N, M = map(int, input().split())
LRC = [tuple(map(int, input().split())) for _ in range(M)]
LRC.sort()

tree = SegmentTree(N, float('inf'), min)
tree.update(0, 0)

for l, r, c in LRC:
    l -= 1
    newDist = tree.query(l, r) + c
    if newDist < tree.query(r - 1, r):
        tree.update(r - 1, newDist)
ans = tree.query(N - 1, N)
print(-1 if ans == float('inf') else ans)