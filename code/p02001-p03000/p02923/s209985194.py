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
    n = gete(int)
    h = tuple(geta(int))

    ans = 0

    cur = 0
    for i in range(n - 1):
        if h[i] >= h[i + 1]:
            cur += 1
            if cur > ans:
                ans = cur
        else:
            cur = 0

    print(ans)


if __name__ == "__main__":
    main()