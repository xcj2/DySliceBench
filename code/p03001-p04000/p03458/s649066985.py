class Acc2D:
    def __init__(self, a):
        h, w = len(a), len(a[0])
        self.acc2D = self._build(h, w, a)

    def _build(self, h, w, a):
        ret = [[0] * (w + 1) for _ in range(h + 1)]
        for r in range(h):
            for c in range(w):
                ret[r + 1][c + 1] = ret[r][c + 1] + ret[r + 1][c] - ret[r][c] + a[r][c]
                # 末項は必要に応じて改変すること
        return ret

    def get(self, r1, r2, c1, c2):
        # [r1,r2), [c1,c2) : 0-indexed
        acc2D = self.acc2D
        return acc2D[r2][c2] - acc2D[r1][c2] - acc2D[r2][c1] + acc2D[r1][c1]


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    g = [[0] * (k * 2) for _ in range(k * 2)]
    for _ in range(n):
        x, y, c_ = input().split()
        x = int(x) % (k * 2)
        y = int(y) % (k * 2)
        if c_ == 'W':
            y = (y + k) % (k * 2)
            # すべて黒にする
        g[y][x] += 1  # WA頂点の存在の有無ではなく、頂点数を数えるので、=1ではなく、+=1

    acc2D = Acc2D(g)

    ret = 0
    # 中央にk*kの区画をとり、黒または白に塗る(条件を満たす個数:黒=s,白=n-s)
    # 4辺を伸ばして、2k*2kの区画を分割し、各区画を評価する
    for r in range(k):  # r+k < k*2
        for c in range(k):  # c+k < k*2
            s = (
                    acc2D.get(0, r, 0, c)
                    + acc2D.get(0, r, c + k, k * 2)
                    + acc2D.get(r, r + k, c, c + k)
                    + acc2D.get(r + k, k * 2, 0, c)
                    + acc2D.get(r + k, k * 2, c + k, k * 2)
            )
            ret = max(ret, s, n - s)

    print(ret)


if __name__ == '__main__':
    main()
