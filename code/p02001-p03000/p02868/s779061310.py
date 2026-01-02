INF = float('inf')

class MinSegTree:
    """
    0-indexed
    query : [L, R)
    """
    def __init__(self, size):
        self.size = 1 << (size.bit_length())  # 完全二分木にする
        self.data = [INF] * (2 * self.size - 1)

    def build(self, rawData):
        self.data[self.size - 1: self.size - 1 + len(rawData)] = rawData
        for i in rawData(self.size - 1)[:: -1]:
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def update(self, index, value):
        index += self.size - 1
        self.data[index] = value
        while index >= 0:
            index = (index - 1) // 2
            self.data[index] = min(self.data[2 * index + 1], self.data[2 * index + 2])

    def query(self, left, right):
        L = left + self.size
        R = right + self.size
        ret = INF
        while L < R:
            if R & 1:
                R -= 1
                ret = min(ret, self.data[R - 1])
            if L & 1:
                ret = min(ret, self.data[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return ret

N, M = map(int, input().split())

LRC = []
for _ in range(M):
    L, R, C = map(int, input().split())
    L -= 1
    LRC.append((L, R, C))
LRC.sort()

tree = MinSegTree(N)
tree.update(0, 0)
for l, r, c in LRC:
    newDist = tree.query(l, r) + c
    oldDist = tree.query(r - 1, r)
    if newDist < oldDist:
        tree.update(r - 1, newDist)

ans = tree.query(N - 1, N)
print(-1 if ans == INF else ans)