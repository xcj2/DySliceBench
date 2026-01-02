class Acc2D:
    def __init__(self, src):
        self.acc2d = self._build(src)

    def _build(self, src):
        h, w = len(src), len(src[0])
        ret = [[0] * w for _ in range(h)]
        for r in range(h):
            for c in range(w):
                ret[r][c] = src[r][c]
                if r > 0:
                    ret[r][c] += ret[r - 1][c]
                if c > 0:
                    ret[r][c] += ret[r][c - 1]
                if r > 0 and c > 0:
                    ret[r][c] -= ret[r - 1][c - 1]
        return ret

    def get(self, r1, c1, r2, c2):
        """[(r1,c1),(r2,c2)]"""
        acc2d = self.acc2d
        ret = acc2d[r2][c2]
        if r1 > 0:
            ret -= acc2d[r1 - 1][c2]
        if c1 > 0:
            ret -= acc2d[r2][c1 - 1]
        if r1 > 0 and c1 > 0:
            ret += acc2d[r1 - 1][c1 - 1]

        return ret


def main():
    import sys

    input = sys.stdin.readline

    N, M, Q = map(int, input().split())

    table = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        L, R = map(int, input().split())
        table[L][R] += 1

    acc2d = Acc2D(table)

    for _ in range(Q):
        p, q = map(int, input().split())
        res = acc2d.get(p, p, q, q)
        print(res)


if __name__ == '__main__':
    main()
