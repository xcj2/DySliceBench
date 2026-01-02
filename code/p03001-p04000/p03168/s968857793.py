

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def read_floats():
    return list(map(float, input().strip().split(' ')))


def solve():
    """
    OPT[N][M] - from N coins having exactly M head
    OPT[N][M] = OPT[N-1][M]*(1-P[N])+OPT[N-1][M-1]*P[N]

    OPT[0][0] = 1
    OPT[i][0] = P[i]
    """
    N = read_int()
    P = read_floats()
    OPT = [
        [0]*(N+1) for _ in range(N+1)
    ]
    OPT[0][0] = 1
    for i in range(1, N+1):
        for j in range(N+1):
            OPT[i][j] = OPT[i-1][j]*(1-P[i-1])
            if j > 0:
                OPT[i][j] += OPT[i-1][j-1]*P[i-1]
    return sum(OPT[-1][(N+1)//2:])


if __name__ == '__main__':
    print(solve())
