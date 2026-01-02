import sys
from math import pi, cos, sqrt
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)
from itertools import permutations


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n = gete(int)
    p = "".join(list(geta()))
    q = "".join(list(geta()))

    base = "".join(map(str, range(1, n + 1)))
    for i, it in enumerate(permutations(base)):
        if p == "".join(it):
            a = i

        if q == "".join(it):
            b = i
    print(abs(b - a))


if __name__ == "__main__":
    main()