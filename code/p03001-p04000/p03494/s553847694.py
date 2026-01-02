def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    return read_int(n)


def read_int(n):
    return list(map(int, read_line().split()[:n]))


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    buf = list(a)
    count = 0
    while True:
        if all(map(lambda x: x % 2 == 0, buf)):
            count += 1
            buf = list(map(lambda x: x // 2, buf))
        else:
            break
    return count
        

def write(result):
    print(result)


if __name__ == '__main__':
    solve()