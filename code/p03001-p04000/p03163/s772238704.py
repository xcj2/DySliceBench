

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[N][W] = maximum value obtained with first N items and weights up to W
    OPT[N][W] = max(OPT[N-1][W-w[N]]+v[N], OPT[N-1][W])
    OPT[0][0] = 0
    """
    N, W = read_ints()
    w, v = [], []
    for _ in range(N):
        w0, v0 = read_ints()
        w.append(w0)
        v.append(v0)
    OPT = [[0]*(W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, W+1):
            OPT[i][j] = OPT[i-1][j]
            if j-w[i-1] >= 0:
                OPT[i][j] = max(OPT[i][j], OPT[i-1][j-w[i-1]]+v[i-1])
    return OPT[-1][-1]


if __name__ == '__main__':
    print(solve())
