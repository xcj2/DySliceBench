

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M, Q = read_ints()
    dp = [ [0 for _ in range(N)] for _ in range(N) ]
    left = [0 for _ in range(N)]
    right = [0 for _ in range(N)]
    length_to_pairs = [[] for _ in range(N)]

    for _ in range(M):
        L, R = read_ints()
        L -= 1
        R -= 1
        length_to_pairs[R-L].append((L, R))
        if L == R:
            dp[L][L] += 1
            right[L] += 1
            left[L] += 1

    for l in range(1, N):
        for i in range(N-l):
            dp[i][i+l] += right[i]+left[i+l]
            if l > 1:
                dp[i][i+l] += dp[i+1][i+l-1]
        for L, R in length_to_pairs[l]:
            dp[L][R] += 1
            right[L] += 1
            left[R] += 1

    for _ in range(Q):
        q0, q1 = read_ints()
        print(dp[q0-1][q1-1])


if __name__ == '__main__':
    solve()
