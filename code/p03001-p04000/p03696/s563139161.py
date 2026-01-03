import math
from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N = read_ints()
    S = input().strip()
    opening = closing = 0
    left_add = 0
    for c in S:
        if c == '(':
            opening += 1
        else:
            closing += 1
        if closing > opening:
            left_add = max(left_add, closing-opening)
    opening = closing = 0
    right_add = 0
    for c in S[::-1]:
        if c == '(':
            opening += 1
        else:
            closing += 1
        if opening > closing:
            right_add = max(right_add, opening-closing)

    return '('*left_add+S+')'*right_add


if __name__ == '__main__':
    print(solve())
