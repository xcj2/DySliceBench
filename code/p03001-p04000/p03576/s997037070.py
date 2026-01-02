from bisect import bisect_left
N, K = map(int, input().split())
Points = []
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    Points.append([x, y])
    X.append(x)
    Y.append(y)

# 座標圧縮
X.sort()
Y.sort()
Points_compressed = []
for x, y in Points:
    cx, cy = bisect_left(X, x), bisect_left(Y, y)
    Points_compressed.append([cx, cy])


class Ruisekiwa2D:
    def __init__(self, h, w):
        self.H = h
        self.W = w
        self.G = [[0] * w for _ in range(h)]

    def load(self, points):
        # 問題によってイメージしやすいよう書き換えてください
        for x, y in points:
            self.G[x][y] += 1

    def load_imos(self, points):
        # pointsは[[左上h, 左上w, 右下h, 右下w], ...]であること
        for i1, j1, i2, j2 in points:
            self.G[i1][j1] += 1  # 左上
            if j2 + 1 < self.W:  # 右上
                self.G[i1][j2+1] -= 1
            if i2 + 1 < self.H:
                self.G[i2+1][j1] -= 1  # 左下
            if j2 + 1 < self.W and i2 + 1 < self.H:  # 右下
                self.G[i2+1][j2+1] += 1

    def calc(self):
        for y in range(self.W):
            for x in range(1, self.H):
                self.G[x][y] += self.G[x-1][y]

        for y in range(1, self.W):
            for x in range(self.H):
                self.G[x][y] += self.G[x][y-1]

    def get(self, i1, j1, i2, j2):
        if i1 > i2 or j1 > j2 or i1 < 0 or j1 < 0 or i2 < 0 or j2 < 0:
            return 0
        elif i1 > 0 and j1 > 0:
            return self.G[i2][j2] - self.G[i1-1][j2] - self.G[i2][j1-1] + self.G[i1-1][j1-1]
        elif i1 <= 0 < j1:
            return self.G[i2][j2] - self.G[i2][j1-1]
        elif j1 <= 0 < i1:
            return self.G[i2][j2] - self.G[i1 - 1][j2]
        else:
            return self.G[i2][j2]


# 二次元累積和
R2D = Ruisekiwa2D(N, N)
R2D.load(Points_compressed)
R2D.calc()


ans = float('inf')
for yi in range(N):
    for yj in range(N):
        for xi in range(N):
            for xj in range(N):
                cx1, cx2 = Points_compressed[xi][0], Points_compressed[xj][0]
                cy1, cy2 = Points_compressed[yi][1], Points_compressed[yj][1]

                x1, x2 = Points[xi][0], Points[xj][0]
                y1, y2 = Points[yi][1], Points[yj][1]

                # 二次元累積和で高速に長方形内部に含まれる点の数を数える
                inside = R2D.get(cx1, cy1, cx2, cy2)
                if inside >= K:
                    ans = min(ans,  abs(x2 - x1) * abs(y2 - y1))

print(ans)
