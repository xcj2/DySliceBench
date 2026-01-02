def solve():
    data = read()
    result = think(data)
    write(result)


def read():
    n = int(input())
    data = []
    for i in range(n):
        data.append(read_data())
    return data


def read_data():
    return list(map(int, input().split(' ')))


def think(data):
    result = []
    for d in data:
        if is_right_triangle(d):
            result.append('YES')
        else:
            result.append('NO')
    return result


def is_right_triangle(d):
    x, y, z = d[0], d[1], d[2]
    return (x ** 2 == y ** 2 + z ** 2) or (y ** 2 == z ** 2 + x ** 2) or (z ** 2 == x ** 2 + y ** 2)


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    solve()
