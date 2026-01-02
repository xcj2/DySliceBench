"""
https://atcoder.jp/contests/abc136/tasks/abc136_b
"""

import math

import numpy as np


def calc(N: int) -> int:
    if N == 0:
        return 0

    keta_suu = calc_ketasuu(N)

    # Nが奇数桁ならその桁の分を考慮
    max_keta_count = N - 10 ** (keta_suu - 1) + 1 if is_odd(keta_suu) else 0

    # i 桁
    other_keta_count = 0
    for keta in range(keta_suu):
        if not is_odd(keta):
            continue
        other_keta_count += 10 ** keta - 10 ** (keta - 1)

    return max_keta_count + other_keta_count


def calc_ketasuu(value: int) -> int:
    return int(math.log10(value) + 1)


def is_odd(value: int) -> bool:
    return value % 2 == 1


def load_input_as_int_array() -> np.ndarray:
    return np.array([int(v) for v in input().split(" ")])


def main() -> None:
    N, = load_input_as_int_array()
    result = calc(N)
    print(result)


main()
