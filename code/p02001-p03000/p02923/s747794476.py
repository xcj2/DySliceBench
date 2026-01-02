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
    h = list(geta(int))
    h += [10**10]

    cur = 0
    ans, tmp = 0, 0
    while cur < n:
        if h[cur] >= h[cur + 1]:
            tmp += 1
        else:
            if tmp > ans:
                ans = tmp
            tmp = 0
        cur += 1
    print(ans)


if __name__ == "__main__":
    main()