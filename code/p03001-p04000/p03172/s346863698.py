

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[N][K] = sum(OPT[N-1][K-i]) 0 <= i <= A[N]
    OPT[0][0] = 1
    N*K
    3 4
    1 2 3

1 0 0 0 0
1 1 0 0 0
1 2 2 1 0
1 3 5 6 5

OPT[3][1] = OPT[2][1]+OPT[2][0]
OPT[3][2] = OPT[2][2]+OPT[2][1]+OPT[2][0]
OPT[3][3] = OPT[2][3]+OPT
    """
    N, K = read_ints()
    A = read_ints()
    modulo = 10**9+7
    OPT = [[0]*(K+1) for _ in range(N+1)]
    for i in range(N+1):
        OPT[i][0] = 1
    for j in range(K+1):
        OPT[0][j] = 1
    for i in range(1, N+1):
        for j in range(1, K+1):
            OPT[i][j] += OPT[i][j-1]+OPT[i-1][j]
            if j-A[i-1]-1 >= 0:
                OPT[i][j] -= OPT[i-1][j-A[i-1]-1]
            OPT[i][j] %= modulo
    if K == 0:
        return OPT[-1][-1]
    return (OPT[-1][-1]-OPT[-1][-2])%modulo


if __name__ == '__main__':
    print(solve())
