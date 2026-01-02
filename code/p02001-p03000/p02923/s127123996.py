"""
https://atcoder.jp/contests/abc139/tasks/abc139_c
"""

import numpy as np


def calc(N: int, H: np.ndarray) -> int:
    return calc_inner(N + 1, np.insert(H, 0, -1))


def calc_inner(N: int, H: np.ndarray) -> int:
    diff = np.diff(H)
    not_movable_mask = diff > 0
    not_movable_index = np.arange(N - 1)[not_movable_mask]
    not_movable_index = np.insert(not_movable_index, len(not_movable_index), N - 1)
    diff_nmi = np.diff(not_movable_index)
    return int(np.max(diff_nmi)) - 1


def load_input_as_int_array() -> np.ndarray:
    return np.array([int(v) for v in input().split(" ")])


def main() -> None:
    N, = load_input_as_int_array()
    H = load_input_as_int_array()
    result = calc(N, H)
    print(result)


main()
