# https://atcoder.jp/contests/abc135/tasks/abc135_b
import numpy as np


def calc(N: int, values: np.ndarray) -> bool:
    sorted_values = np.sort(values)
    difference = sorted_values != values
    difference_count = difference.sum()
    return difference_count == 0 or difference_count == 2


def load_input_as_int_array() -> np.ndarray:
    return np.array([int(v) for v in input().split(" ")])


def main() -> None:
    N = load_input_as_int_array()
    values = load_input_as_int_array()
    result = calc(N, values)
    result_str = "YES" if result else "NO"
    print(result_str)


main()
