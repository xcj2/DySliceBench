def main():
    import itertools
    import os
    import sys

    if os.getenv("LOCAL"):
        sys.stdin = open("_in.txt", "r")

    sys.setrecursionlimit(10 ** 9)
    INF = float("inf")
    IINF = 10 ** 18
    MOD = 10 ** 9 + 7


    # MOD = 998244353


    def cumsum(it):
        """
        累積和
        :param collections.Iterable it:
        """
        cs = 0
        ret = [0]
        for v in it:
            cs += v
            ret.append(cs)
        return ret


    def cumsum_mat(mat):
        h = len(mat)
        w = len(mat[0])

        tmp = []
        for row in mat:
            tmp.append(cumsum(row))
        del mat

        ret = [[0] * (w + 1) for _ in range(h + 1)]
        for c in range(w + 1):
            col = [row[c] for row in tmp]
            for r, a in enumerate(cumsum(col)):
                ret[r][c] = a
        return ret


    N, M, Q = list(map(int, sys.stdin.buffer.readline().split()))
    S = [list(map(int, sys.stdin.buffer.readline().decode().rstrip())) for _ in range(N)]
    XY = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(Q)]


    def count_v(x1, y1, x2, y2):
        return counts_cum[x2][y2] - counts_cum[x1 - 1][y2] - counts_cum[x2][y1 - 1] + counts_cum[x1 - 1][y1 - 1]


    def count_ev(x1, y1, x2, y2):
        return edges_v_cum[x2][y2] - edges_v_cum[x1][y2] - edges_v_cum[x2][y1 - 1] + edges_v_cum[x1][y1 - 1]


    def count_eh(x1, y1, x2, y2):
        return edges_h_cum[x2][y2] - edges_h_cum[x1 - 1][y2] - edges_h_cum[x2][y1] + edges_h_cum[x1 - 1][y1]


    vs = []
    e1 = []
    e2 = []

    counts_cum = cumsum_mat(S)
    for x1, y1, x2, y2 in XY:
        vs.append(count_v(x1, y1, x2, y2))
    del counts_cum

    edges_v = [[0] * M for _ in range(N)]
    for h, w in itertools.product(range(1, N), range(M)):
        edges_v[h][w] = S[h][w] & S[h - 1][w]
    edges_v_cum = cumsum_mat(edges_v)
    for x1, y1, x2, y2 in XY:
        e1.append(count_ev(x1, y1, x2, y2))
    del edges_v
    del edges_v_cum

    edges_h = [[0] * M for _ in range(N)]
    for h, w in itertools.product(range(N), range(1, M)):
        edges_h[h][w] = S[h][w] & S[h][w - 1]
    edges_h_cum = cumsum_mat(edges_h)
    for x1, y1, x2, y2 in XY:
        e2.append(count_eh(x1, y1, x2, y2))
    del edges_h
    del edges_h_cum

    ans = [v - e1 - e2 for v, e1, e2 in zip(vs, e1, e2)]
    print(*ans, sep='\n')


main()
