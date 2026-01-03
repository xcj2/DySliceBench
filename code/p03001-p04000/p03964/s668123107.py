def solve():
    list_t_and_a = read()
    result = think(list_t_and_a)
    write(result)


def read():
    n = read_int(1)[0]
    list_t_and_a = []
    for _ in range(n):
        list_t_and_a.append(read_int(2))
    return list_t_and_a


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(list_t_and_a):
    n = len(list_t_and_a)
    vote_t, vote_a = list_t_and_a[0][0], list_t_and_a[0][1]
    for i in range(1, n):
        ti, ai = list_t_and_a[i][0], list_t_and_a[i][1]
        ratio_t = vote_t // ti
        if vote_t % ti != 0:
            ratio_t += 1
        ratio_a = vote_a // ai
        if vote_a % ai != 0:
            ratio_a += 1
        ratio = max(ratio_t, ratio_a)
        vote_t = ratio * ti
        vote_a = ratio * ai
    return vote_t + vote_a


def expected_lower_value_than_actual(actual, expected):
    return actual > expected


def write(result):
    print(result)


if __name__ == '__main__':
    solve()