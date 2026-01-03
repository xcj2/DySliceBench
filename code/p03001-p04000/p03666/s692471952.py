import sys

# sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve_it0(n, a, b, c, d):
    p = [[0]]
    for i in range(1, n):
        q = set()
        for x in p[-1]:
            for k in range(c, d + 1):
                q.add(x - k)
                q.add(x + k)
        p.append(sorted(q))
    for l in p:
        print(l)
    if b - a in p[-1]:
        return 'YES'
    return 'NO'


def solve_it1(n, a, b, c, d):
    x = b - a
    for i in range(n + 1):
        left = - i * d + (n - 1 - i) * c
        right = - i * c + (n - 1 - i) * d
        if left <= x <= right:
            return 'YES'
    return 'NO'


def solve():
    n, a, b, c, d = read_int_list()
    res1 = solve_it1(n, a, b, c, d)
    # res0 = solve_it0(n, a, b, c, d)
    # assert res0 == res1
    return res1


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
