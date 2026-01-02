

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[i][j] = X-Y value, between i and j
    OPT[i][j] = max(A[i]-OPT[i+1][j], A[j]-OPT[i][j-1])
    OPT[i][i] = A[i]
    """
    N = read_int()
    A = read_ints()
    OPT = [
        [0]*N for _ in range(N)
    ]
    for i in range(N):
        OPT[i][i] = A[i]
    for length in range(1, N):
        for i in range(N-length):
            OPT[i][i+length] = max(A[i]-OPT[i+1][i+length],
                                   A[i+length]-OPT[i][i+length-1])
    return OPT[0][-1]


if __name__ == '__main__':
    print(solve())
