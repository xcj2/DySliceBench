

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[i][j][k] - sum is i, j number of elements, first k elements
    OPT[i][j][k] = OPT[i-x[k]][j-1][k-1] if j-th element is taken
                   OPT[i][j][k-1]

    OPT[A*j][j][k] for all k
    """
    N, A = read_ints()
    x = read_ints()
    OPT = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(2501)]
    for k in range(N+1):
        OPT[0][0][k] = 1
    for i in range(len(OPT)):
        for j in range(1, N+1):
            for k in range(1, N+1):
                if i-x[k-1] >= 0:
                    OPT[i][j][k] += OPT[i-x[k-1]][j-1][k-1]
                OPT[i][j][k] += OPT[i][j][k-1]
    T = 0
    for j in range(1, N+1):
        T += OPT[A*j][j][N]
    return T


if __name__ == '__main__':
    print(solve())
