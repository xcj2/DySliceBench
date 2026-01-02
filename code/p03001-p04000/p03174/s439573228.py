

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def count_bits(N):
    T = 0
    while N != 0:
        T += N & 1
        N >>= 1
    return T


def solve():
    """
    OPT[i][j] - number of pairs for first i man, with mask j=0011..01

    OPT[i+1][j|k] += OPT[i][j] k has exactly one bit set j|k != j and i+1 is compatible with k-th woman

    """
    N = read_int()
    modulo = 10**9+7
    A = []
    for _ in range(N):
        A.append(read_ints())
    dp = [0]*(2**N)
    dp[0] = 1
    for mask in range(2**N-1):
        a = count_bits(mask)
        for b in range(N):
            if A[a][b] and mask&(1<<b) == 0:
                dp[mask|(1<<b)] = (dp[mask|(1<<b)]+dp[mask])%modulo
    return dp[-1]


if __name__ == '__main__':
    print(solve())
