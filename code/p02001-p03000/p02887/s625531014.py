def solve():
    data = read()
    result = think(data)
    write(result)


def read():
    n = read_int(1)[0]
    return read_line(n)


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(data):
    count = 0
    current_char = ''
    for i in range(len(data)):
        if current_char == data[i]:
            continue
        current_char = data[i]
        count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    # import sys
    # sys.setrecursionlimit(10000)
    solve()
