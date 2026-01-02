#!/usr/bin/env pypy3


def get_line():
    return input()


def get_tokens():
    return get_line().split()


def get_ints():
    return [int(_) for _ in get_tokens()]


from collections import defaultdict


def main():
    n, = get_ints()
    v = get_ints()

    tot = [0, 0]
    cnt = [defaultdict(int), defaultdict(int)]

    for i in range(n):
        tot[i % 2] += 1
        cnt[i % 2][v[i]] += 1

    p = [[], []]
    for r in [0, 1]:
        p[r] = [(v, k) for k, v in cnt[r].items()] + [(0, -1 - r)]
        p[r].sort()
        p[r] = p[r][-2:]

    ans = n

    for x in p[0]:
        for y in p[1]:
            if x[1] != y[1]:
                ans = min(ans, n - x[0] - y[0])

    print(ans)


if __name__ == '__main__':
    main()