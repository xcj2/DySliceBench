def solve():
    k, a = read()
    result = think(k, a)
    write(result)


def read():
    n, k = read_int(2)
    a = read_int(n)
    return k, a


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(k, a):
    max_n = 100

    # dp[i] = True/False; True means First player win if num of stone is i
    dp = [False] * (k + max_n + 1)

    for i in range(len(dp)):
        for elem in a:
            if i >= elem:
                dp[i] |= not dp[i - elem]

    return dp[k]


def write(result):
    if result:
        print('First')
    else:
        print('Second')


if __name__ == '__main__':
    solve()