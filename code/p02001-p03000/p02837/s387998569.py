#!/usr/bin/env python3
from itertools import product


def read_data():
    N = int(input())
    testimonies = []

    for _ in range(N):
        A = int(input())
        testimonies_i = []

        for _ in range(A):
            x, y = map(int, input().split())
            testimonies_i.append((x - 1, y))  # 0-based

        testimonies.append(testimonies_i)

    return N, testimonies


def is_honest(pattern, i):
    # i番目の人が正直者であるか (0-based)
    return pattern[i]


def contradiction_exists(pattern, testimonies_i):
    # ある人の複数の証言に矛盾があるか
    for x, y in testimonies_i:
        if is_honest(pattern, x) != y:
            return True

    return False


def is_valid_pattern(pattern, testimonies):
    for i, p in enumerate(pattern):
        if not is_honest(pattern, i):
            continue

        if contradiction_exists(pattern, testimonies[i]):
            return False

    return True


def solve():
    N, testimonies = read_data()
    max_honest = 0

    for pattern in product([0, 1], repeat=N):
        # N=3 => [(0,0,0), (0,0,1), ..., (1,1,1)]
        if is_valid_pattern(pattern, testimonies):
            count_honest = sum(pattern)
            if count_honest > max_honest:
                max_honest = count_honest

    print(max_honest)


if __name__ == "__main__":
    solve()
