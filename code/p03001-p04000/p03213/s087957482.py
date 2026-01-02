#!/usr/bin/env python3
from collections import Counter
from functools import reduce
from itertools import permutations
import sys

try:
    from typing import Set, Tuple
except ImportError:
    pass


def factor(n: int):
    k = 2
    while n % k == 0:
        n //= k
        yield k
    k = 3
    while n != 1:
        while n % k == 0:
            n //= k
            yield k
        k += 2


def solve(N: int):
    m = reduce(
        lambda a, b: a + b,
        (
            Counter(factor(i))
            for i in range(1, N + 1)
        )
    )
    # 75 = 3 * 5 * 5 = 3 * 25 = 15 * 5
    qss = [
        [74],
        [2, 4, 4],
        [2, 24],
        [4, 14],
    ]
    nums = set()  # type: Set[Tuple[Tuple[int, int], ...]]
    for qs in qss:
        for ps in permutations(m.keys(), len(qs)):
            if any(m[p] < q for p, q in zip(ps, qs)):
                continue
            num = sorted(zip(ps, qs))
            nums.add(tuple(num))
    print(len(nums))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
