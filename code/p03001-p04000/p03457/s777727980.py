def solve():
    list_of_txy = read()
    result = think(list_of_txy)
    write(result)


def read():
    n = read_int(1)[0]
    list_of_txy = [[0, 0, 0]]
    for _ in range(n):
        list_of_txy.append(read_int(3))
    return list_of_txy


def read_int(n):
    return list(map(int, read_line().split()[:n]))


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(list_of_txy):
    for i in range(len(list_of_txy) - 1):
        t, x, y = list_of_txy[i]
        nt, nx, ny = list_of_txy[i + 1]
        dx, dy, dt = abs(nx - x), abs(ny - y), abs(nt - t)
        if dx + dy > dt:
            return False
        if (dt - dx - dy) % 2 != 0:
            return False
    return True


def write(result):
    if result:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()