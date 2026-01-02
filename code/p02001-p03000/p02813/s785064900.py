"""
https://atcoder.jp/contests/abc150/tasks/abc150_c
"""
import numpy as np
from itertools import permutations


def calc(N: int, P: np.ndarray, Q: np.ndarray) -> int:
    pairs = list(permutations(range(1, N + 1)))
    pairs_dict = {tuple(v): i for i, v in enumerate(pairs)}
    return abs(pairs_dict[tuple(P)] - pairs_dict[tuple(Q)])


def load_input_as_int_array() -> np.ndarray:
    return np.array([int(v) for v in input().split(" ")])


def main() -> None:
    N, = load_input_as_int_array()
    P = load_input_as_int_array()
    Q = load_input_as_int_array()
    result = calc(N, P, Q)
    print(result)


main()
