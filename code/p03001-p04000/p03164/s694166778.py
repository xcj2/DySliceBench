def solve():
    max_weight, list_of_weight_and_value = read()
    result = think(max_weight, list_of_weight_and_value)
    write(result)


def read():
    n, max_weight = read_int(2)
    list_of_weight_and_value = []
    for i in range(n):
        list_of_weight_and_value.append(read_int(2))
    return max_weight, list_of_weight_and_value


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(max_weight, list_of_weight_and_value):
    MAX_WEIGHT = 10 ** 9
    MAX_VALUE = 10 ** 3
    MAX_N = 100
    INVALID_VALUE = MAX_WEIGHT * MAX_N + 1

    # dp[v] means minimum weight achieves total value 'v'
    dp = [INVALID_VALUE for x in range(MAX_VALUE * len(list_of_weight_and_value) + 1)]
    dp[0] = 0

    for weight, value in list_of_weight_and_value:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] != INVALID_VALUE and i + value < len(dp):
                if dp[i + value] == INVALID_VALUE:
                    dp[i + value] = dp[i] + weight
                else:
                    dp[i + value] = min(dp[i + value], dp[i] + weight)
    for i in range(len(dp) - 1, -1, -1):
        if dp[i] != INVALID_VALUE and dp[i] <= max_weight:
            return i


def write(result):
    print(result)


if __name__ == '__main__':
    solve()