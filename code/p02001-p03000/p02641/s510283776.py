import sys
from math import pi, cos, sqrt
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    x, n = geta(int)
    p = set(tuple(geta(int)))

    if x not in p:
        print(x)
        return

    x1 = x - 1
    x2 = x + 1

    while True:
        if x1 not in p:
            print(x1)
            return

        if x2 not in p:
            print(x2)
            return

        x1 -= 1
        x2 += 1


if __name__ == "__main__":
    main()