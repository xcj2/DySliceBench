import sys

# sys.stdin = open('d1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    h, w = read_int_list()
    n = read_int()
    a = read_int_list()
    c = [[0] * w for i in range(h)]
    color = [0] * (w * h)
    t = 0
    for k in range(n):
        for l in range(a[k]):
            color[t] = k + 1
            t += 1
    t = 0
    for i in range(h):
        if i % 2 == 1:
            for j in range(w):
                c[i][j] = color[t]
                t += 1
        else:
            for j in range(w - 1, -1, -1):
                c[i][j] = color[t]
                t += 1
    for i in range(h):
        for j in range(w):
            print(c[i][j], end='')
            end = ' '
            if j == w - 1:
                end = '\n'
            print(end=end)
    return 0


def main():
    res = solve()


if __name__ == '__main__':
    main()
