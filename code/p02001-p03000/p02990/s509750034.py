

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def ilen(it):
    return sum(1 for _ in it)


def solve():
    """
    C[N-K+1][i]*C[K-1][i-1]
    1 1 1
    1 2 3
    1 3 6
    """
    N, K = read_ints()
    C = [
        [0 for _ in range(2002)] for _ in range(2002)
    ]
    modulo = 10**9+7
    C[1][1] = 1
    for i in range(2, 2002):
        for j in range(1, i+1):
            C[i][j] = (C[i-1][j]+C[i-1][j-1])%modulo

    for i in range(1, K+1):
        print((C[N-K+1+1][i+1]*C[K-1+1][i-1+1])%modulo)


if __name__ == '__main__':
    solve()
