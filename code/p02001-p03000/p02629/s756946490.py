import sys

from typing import List


def _10_to_26(number: int) -> List[str]:
    if number // 26:
        division = number // 26
        remain = number % 26

        if remain is 0:
            if division == 1:
                return ['z']

            return _10_to_26(number // 26 - 1) + ['z']

        _ = _10_to_26(number // 26)
        _.append(
            to_char(remain)
        )
        return _
    return [
        to_char(number % 26)
    ]


def to_char(num: int) -> str:
    return chr(ord('a') - 1 + num)


def main() -> None:
    N = int(input())
    print(''.join(_10_to_26(N)))


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()
