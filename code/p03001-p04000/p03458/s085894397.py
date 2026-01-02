from itertools import product

N, K = map(int, input().split())
kk = K * 2


class CumSum2d(object):
    def __init__(self, H, W):
        self.H, self.W = H, W
        self.tiles = [[0] * W for _ in range(H)]

    def add(self, x, y, c=1):
        self.tiles[y][x] += c

    def build(self):
        for y in range(self.H):
            for x in range(1, self.W):
                self.tiles[y][x] += self.tiles[y][x - 1]
        for y in range(1, self.H):
            for x in range(self.W):
                self.tiles[y][x] += self.tiles[y - 1][x]

    def get(self, sx, sy, tx, ty):
        assert sx <= tx and sy <= ty
        cnt = self.tiles[ty][tx]
        if sx > 0:
            cnt -= self.tiles[ty][sx - 1]
        if sy > 0:
            cnt -= self.tiles[sy - 1][tx]
        if sx > 0 and sy > 0:
            cnt += self.tiles[sy - 1][sx - 1]
        return cnt


cs = CumSum2d(kk, kk)
for i in range(N):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == 'B':
        y += K
    cs.add(x % kk, y % kk)
cs.build()

ans = 0
for x, y in product(range(K), repeat=2):
    cnt = cs.get(x, y, x + K - 1, y + K - 1)
    cnt += cs.get(x + K, y + K, kk - 1, kk - 1)
    if x > 0:
        cnt += cs.get(0, y + K, x - 1, kk - 1)
    if y > 0:
        cnt += cs.get(x + K, 0, kk - 1, y - 1)
    if x > 0 and y > 0:
        cnt += cs.get(0, 0, x - 1, y - 1)
    ans = max(ans, cnt, N - cnt)
print(ans)