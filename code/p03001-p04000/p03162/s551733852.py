def solve():
    list_of_abc = read()
    result = think(list_of_abc)
    write(result)


def read():
    n = read_int(1)[0]
    list_of_abc = []
    for i in range(n):
        list_of_abc.append(read_int(3))
    return list_of_abc


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(list_of_abc):
    dp = [[0 for abc in range(3)] for n in range(len(list_of_abc))]
    dp[0][0] = list_of_abc[0][0]
    dp[0][1] = list_of_abc[0][1]
    dp[0][2] = list_of_abc[0][2]

    for i in range(1, len(list_of_abc)):
        dp[i][0] = max(dp[i - 1][1] + list_of_abc[i][0], dp[i - 1][2] + list_of_abc[i][0])
        dp[i][1] = max(dp[i - 1][0] + list_of_abc[i][1], dp[i - 1][2] + list_of_abc[i][1])
        dp[i][2] = max(dp[i - 1][0] + list_of_abc[i][2], dp[i - 1][1] + list_of_abc[i][2])

    return max(dp[-1][0], dp[-1][1], dp[-1][2])


def write(result):
    print(result)


if __name__ == '__main__':
    solve()