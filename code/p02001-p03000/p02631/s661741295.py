#!/usr/bin/env python3


def main() -> None:
    N = ri()
    a = rmi()
    assert len(a) == N
    result = []
    all_xor = 0
    for item in a:
        all_xor ^= item
    for item in a:
        result.append(item ^ all_xor)
    w(' '.join(map(str, result)))


def r() -> str:
    return input().strip()


def ri() -> int:
    return int(r())


def rmi(delim: str = ' ') -> tuple:
    return tuple(map(int, input().split(delim)))


def w(data) -> None:
    print(data)


def wm(*data, delim: str = ' ') -> None:
    print(delim.join(map(str, data)))


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10 ** 9)
    main()
