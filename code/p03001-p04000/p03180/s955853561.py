

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N = read_int()
    A = []
    for i in range(N):
        A.append(read_ints())
    base = [0]*(2**N)
    for i in range(2**N):
        for j in range(N):
            for k in range(j):
                if i & (1<<j) and i & (1<<k):
                    base[i] += A[j][k]
    dp = [0]*(2**N)
    for i in range(2**N):
        j = i
        while j > 0:
            dp[i] = max(dp[i], dp[i-j]+base[j])
            j = (j-1)&i
    return dp[2**N-1]


if __name__ == '__main__':
    print(solve())
