import sys
from itertools import permutations
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    N = readint()
    P = tuple(readnums())
    Q = tuple(readnums())

    a = b = 0
    for i, v in enumerate(permutations(range(1, N + 1))):
        if v == P:
            a = i
        if v == Q:
            b = i

    print(abs(a - b))


if __name__ == "__main__":
    main()
