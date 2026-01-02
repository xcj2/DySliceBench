

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[value] - minimum weight that achieves value
    OPT[value] = OPT[value-v[i]]
    """
    N, W = read_ints()
    max_value = 1000*N+1
    dp = [10**12+1]*max_value
    dp[0] = 0
    for i in range(N):
        w, v = read_ints()
        for j in range(max_value-1, -1, -1):
            if j >= v:
                dp[j] = min(dp[j], dp[j-v]+w)
    ans = 0
    for j in range(max_value):
        if dp[j] <= W:
            ans = j
    return ans


if __name__ == '__main__':
    print(solve())
