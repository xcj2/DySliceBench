

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def merge(N, modulo, A, B):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for j0 in range(N):
                C[i][j] = (C[i][j]+A[i][j0]*B[j0][j])%modulo
    return C


def solve():
    """
    OPT[k][i][j] - number of ways from i to j in K step
    OPT[1] = A

    OPT[k] = 
    """
    N, K = read_ints()
    A = []
    modulo = 10**9+7
    for _ in range(N):
        A.append(read_ints())
    def opt(k):
        if k == 1:
            return A
        half = opt(k//2)
        answer = merge(N, modulo, half, half)
        if k%2 == 1:
            answer = merge(N, modulo, answer, A)
        return answer
    return sum(c for row in opt(K) for c in row)%modulo


if __name__ == '__main__':
    print(solve())
