import gc


class Ruiseki2D():
    """二次元累積和を構築する
    構築O(HW), 区間取得クエリO(1)
    """
    def __init__(self, matrix):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.ruiseki = [[0] * (self.w + 1) for _ in range(self.h + 1)]

        for i in range(self.h):
            for j in range(self.w):
                self.ruiseki[i + 1][j + 1] = self.ruiseki[i + 1][j] + matrix[i][j]
        for i in range(self.h):
            for j in range(self.w):
                self.ruiseki[i + 1][j + 1] += self.ruiseki[i][j + 1]

    def get_sum(self, hl, hr, wl, wr):
        """[hl, hr), [wl, wr) で囲まれた部分の和を求める"""
        return self.ruiseki[hr][wr] + self.ruiseki[hl][wl] - self.ruiseki[hr][wl] - self.ruiseki[hl][wr]


n, m, q = map(int, input().split())
s = [list(map(int, input())) for i in range(n)]
query = [list(map(int, input().split())) for i in range(q)]

ru_col_cnt = Ruiseki2D(s)

# メモリ削減のため累積和配列を使い回す
yoko_edge = [[0] * (m + 1) for i in range(n + 1)]
for i in range(n):
    for j in range(m - 1):
        if s[i][j] == 1 and s[i][j + 1] == 1:
            yoko_edge[i + 1][j + 1] = 1
for i in range(n):
    for j in range(m):
        yoko_edge[i + 1][j + 1] += yoko_edge[i + 1][j]
for i in range(n):
    for j in range(m):
        yoko_edge[i + 1][j + 1] += yoko_edge[i][j + 1]

tate_edge = [[0] * (m + 1) for i in range(n + 1)]
for i in range(n - 1):
    for j in range(m):
        if s[i][j] == 1 and s[i + 1][j] == 1:
            tate_edge[i + 1][j + 1] = 1
for i in range(n):
    for j in range(m):
        tate_edge[i + 1][j + 1] += tate_edge[i + 1][j]
for i in range(n):
    for j in range(m):
        tate_edge[i + 1][j + 1] += tate_edge[i][j + 1]



def yoko_get_sum(hl, hr, wl, wr):
    return yoko_edge[hr][wr] + yoko_edge[hl][wl] - yoko_edge[hr][wl] - yoko_edge[hl][wr]
  
def tate_get_sum(hl, hr, wl, wr):
    return tate_edge[hr][wr] + tate_edge[hl][wl] - tate_edge[hr][wl] - tate_edge[hl][wr]

for hl, wl, hr, wr in query:
    hl, wl = hl - 1, wl - 1
    ans = ru_col_cnt.get_sum(hl, hr, wl, wr)
    ans -= yoko_get_sum(hl, hr, wl, wr - 1) + tate_get_sum(hl, hr - 1, wl, wr)
    print(ans)
