#!/usr/bin/env python3

import bisect


M = 4472


def generate_triangle_numbers(max_idx=M):
    assert max_idx >= 0
    for i in range(max_idx + 1):
        yield i * (i + 1) // 2


def decompose(n):
    tris = list(generate_triangle_numbers())
    # T[i - 1] < n <= T[i]
    i = bisect.bisect_left(tris, n)
    t = tris[i]
    if t == n:
        return list(range(1, i + 1))
    else:
        for j in range(1, i):
            if t - j == n:
                return list(range(1, j)) + list(range(j + 1, i + 1))


def main():
    xs = decompose(int(input()))
    print(*xs, sep="\n")


if __name__ == '__main__':
    main()
