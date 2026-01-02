from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def ceil(A, B):
    if A%B == 0:
        return A//B
    return A//B+1

def solve() -> Any:
    N = read_int()
    C, S, F = [], [], []
    for _ in range(N-1):
        c, s, f = read_ints()
        C.append(c)
        S.append(s)
        F.append(f)
    dp = [
        [0 for _ in range(N)] for _ in range(N)
    ]
    # dp[i][j] - minimum time for i-th train to arrive at j-th station
    for j in range(1, N):
        for i in range(j):
            if dp[i][j-1] <= S[j-1]:
                dp[i][j] = S[j-1]+C[j-1]
            else:
                k = ceil((dp[i][j-1]-S[j-1]), F[j-1])
                dp[i][j] = k*F[j-1]+S[j-1]+C[j-1]
                # k*F[j-1]+S[j-1] >= dp[i][j-1]
    for i in range(N):
        print(dp[i][N-1])


if __name__ == '__main__':
    solve()
