

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


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
        half_A = opt(k//2)
        new_A = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for j0 in range(N):
                    new_A[i][j] = (new_A[i][j]+half_A[i][j0]*half_A[j0][j])%modulo
        if k%2 == 0:
            return new_A
        new_A2 = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for j0 in range(N):
                    new_A2[i][j] = (new_A2[i][j]+new_A[i][j0]*A[j0][j])%modulo
        return new_A2
    return sum(c for row in opt(K) for c in row)%modulo



if __name__ == '__main__':
    print(solve())
