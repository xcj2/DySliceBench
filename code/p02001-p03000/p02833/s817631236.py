import math
from typing import List, Counter, Tuple
from collections import Counter
from itertools import permutations, zip_longest, groupby


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> int:
    # f(n) = 1, n < 2
    # f(n) = n*f(n-2) n>= 2
    N = read_int()
    if N%2 == 1:
        return 0
    answer = 0
    base = 10
    while base <= N:
        answer += N//base
        base *= 5
    return answer


if __name__ == '__main__':
    print(solve())
