def main():
    import sys

    input = sys.stdin.readline

    def build_table(h, w, a):
        ret = [[0] * (w + 1) for _ in range(h + 1)]
        for r in range(h):
            for c in range(w):
                ret[r + 1][c + 1] = ret[r + 1][c] + ret[r][c + 1] - ret[r][c] + a[r][c]
        return ret

    def get(p, q, t):
        return t[q][q] - t[p - 1][q] - t[q][p - 1] + t[p - 1][p - 1]

    n, m, q = map(int, input().split())

    t = [[0] * (n + 1) for _ in range(n + 1)]  # 0-indexed
    for _ in range(m):
        l, r = (int(x) - 1 for x in input().split())  # 0-indexed
        t[l][r] += 1

    t = build_table(n, n, t)  # 1-indexed

    ret = []
    for _ in range(q):
        p, q = map(int, input().split())  # 1-indexed
        ret.append(get(p, q, t))

    print(*ret, sep='\n')


if __name__ == '__main__':
    main()
