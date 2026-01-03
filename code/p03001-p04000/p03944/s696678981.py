

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    W, H, N = read_ints()
    x0, y0, x1, y1 = 0, 0, W, H
    for _ in range(N):
        x, y, a = read_ints()
        if a == 1:
            x0 = min(max(x, x0), x1)
        if a == 2:
            x1 = max(min(x, x1), x0)
        if a == 3:
            y0 = min(max(y, y0), y1)
        if a == 4:
            y1 = max(min(y, y1), y0)
    return (x1-x0)*(y1-y0)


if __name__ == '__main__':
    print(solve())
