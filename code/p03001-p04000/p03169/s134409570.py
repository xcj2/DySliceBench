def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    n = len(a)
    count_1 = a.count(1)
    count_2 = a.count(2)
    count_3 = a.count(3)

    # dp[count_1][count_2][count_3] = expectation of attempts for all dishes are cleared
    expectation_of_attempts = [[[0.0 for num_dishes_3 in range(n + 1)] for num_dishes_2 in range(n + 1)] for num_dishes_1 in range(n + 1)]

    for k in range(count_3 + 1):
        for j in range(count_2 + count_3 + 1):
            if j + k > n:
                continue
            for i in range(n + 1):
                if i + j + k > n:
                    continue
                if i == 0 and j == 0 and k == 0:
                    continue
                if expectation_of_attempts[i][j][k] > 0.0:
                    return expectation_of_attempts[i][j][k]
                a = 0.0 if i == 0 else expectation_of_attempts[i - 1][j][k]
                b = 0.0 if j == 0 else expectation_of_attempts[i + 1][j - 1][k]
                c = 0.0 if k == 0 else expectation_of_attempts[i][j + 1][k - 1]

                expectation_of_attempts[i][j][k] = (i * a + j * b + k * c + n) / (i + j + k)

    return expectation_of_attempts[count_1][count_2][count_3]


def write(result):
    print(result)


if __name__ == '__main__':
    solve()