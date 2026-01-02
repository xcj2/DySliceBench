"""
https://atcoder.jp/contests/abc136/tasks/abc136_c
"""

import numpy as np


def calc(N: int, values: np.ndarray) -> bool:
    # 要素が1つなら確定でOK
    if len(values) == 1:
        return True

    # 2つ以上下がっている部分があるとNG
    gradient = np.diff(values)
    if np.min(gradient) <= -2:
        return False

    # 要素が2つでならこの時点でOK確定
    if len(values) == 2:
        return True

    # 1つ下がってから、上がる前に、1つ下がるとNG
    gradient_without_zero = gradient[gradient != 0]
    if len(gradient_without_zero) == 0:
        return True
    gradient_without_last = gradient_without_zero[:-1]
    gradient_without_first = gradient_without_zero[1:]
    if np.min(gradient_without_first + gradient_without_last) <= -2:
        return False
    return True


def load_input_as_int_array() -> np.ndarray:
    return np.array([int(v) for v in input().split(" ")])


def main() -> None:
    N, = load_input_as_int_array()
    values = load_input_as_int_array()
    result = calc(N, values)
    print("Yes" if result else "No")


main()
