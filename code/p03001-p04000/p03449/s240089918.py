#■標準入力ショートカット


def get_next_int():
    return int(float(input()))


def get_next_ints(delim=" "):
    return tuple([int(float(x)) for x in input().split(delim)])


def get_next_str():
    return input()


def get_next_strs(delim=" "):
    return tuple(input().split(delim))


def get_next_by_types(*value_types, delim=" "):
    return tuple([t(x) for t, x in zip(value_types, input().split(delim))])


def solve():
    N = get_next_int()
    upper_line = get_next_ints()
    lower_line = get_next_ints()

    up_dp = [0]*N
    low_dp = [0]*N

    up_dp[0] = upper_line[0]
    low_dp[N-1] = lower_line[N-1]
    for i in range(1, N):
        up_dp[i] = up_dp[i-1] + upper_line[i]
        low_dp[N-i-1] = low_dp[N-i] + lower_line[N-i-1]
    max_candies = 0
    for i in range(N):
        max_candies = max(max_candies, up_dp[i] + low_dp[i])
    print(max_candies)

solve()