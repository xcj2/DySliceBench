def solve():
    data = read()
    result = think(data)
    write(result)


def read():
    return [read_line(), read_line()]


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
    d1, d2 = data[0], data[1]
    count = 0
    for i in range(len(d1)):
        if d1[i] == d2[i]:
            count += 1
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    solve()