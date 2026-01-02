def solve():
    s = read()
    result = think(s)
    write(result)


def read():
    return read_line()


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(s):
    local_s = 'L' + s
    n = len(local_s)
    symbol_right = 'R'
    symbol_left = 'L'
    steps = 10 ** 100

    steps_to_turning_point = [0 for x in range(n)]
    turning_point_from = [[0, 0] for x in range(n)]
    count = [0 for x in range(n)]

    index = 0
    from_x = 1
    to_x = 2
    while True:
        while to_x < n and local_s[from_x] == local_s[to_x]:
            to_x += 1
        # print('debug', from_x, to_x)
        if s[from_x] == symbol_right:
            for i in range(from_x, to_x):
                if ((steps - abs(to_x - i)) % 2 == 0):
                    # print('case 1,', i, to_x, abs(to_x - i))
                    count[to_x] += 1
                else:
                    # print('case 2,', i, to_x - 1, abs(to_x - i))
                    count[to_x - 1] += 1
        else:
            for i in range(from_x, to_x):
                if ((steps - abs(i - index)) % 2 == 0):
                    # print('case 3,', i, index)
                    count[index] += 1
                else:
                    # print('case 4,', i, index + 1)
                    count[index + 1] += 1
        index = to_x - 1
        from_x = to_x
        to_x += 1

        if to_x >= n:
            break

    # print('last,', from_x, to_x, index)
    # should be left symbol
    if from_x < n:
        for i in range(from_x, to_x):
            if ((steps - abs(i - index)) % 2 == 0):
                # print('case 5,', i, index)
                count[index] += 1
            else:
                # print('case 6,', i, index + 1)
                count[index + 1] += 1
    return count[1:]


def find_turning_point(s, what, symbol_left, symbol_right, from_x):
    if what == symbol_left:
        turning_point_from = s.find(symbol_left, from_x)
        return turning_point_from, turning_point_from - 1
    else:
        turning_point_from = s[:from_x].rfind(symbol_right)
        return turning_point_from, turning_point_from + 1


def write(result):
    print(' '.join(list(map(str, result))))


if __name__ == '__main__':
    solve()