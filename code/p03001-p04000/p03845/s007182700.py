import sys

# sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    n = read_int()
    t = read_int_list()
    m = read_int()
    p = [0] * m
    x = [0] * m
    for i in range(m):
        p[i], x[i] = read_int_list()
        p[i] -= 1

    for i in range(m):
        res = 0
        for j in range(n):
            if j == p[i]:
                time = x[i]
            else:
                time = t[j]
            res += time
        print(res)


main()
