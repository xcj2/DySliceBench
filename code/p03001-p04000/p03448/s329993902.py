import sys
from math import sqrt
from collections import Counter

input = sys.stdin.readline


def I():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    a = I()
    b = I()
    c = I()
    x = I()

    result = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                total = 500 * i + 100 * j + 50 * k
                if x == total:
                    result += 1
    print(result)
    pass


if __name__ == "__main__":
    main()
