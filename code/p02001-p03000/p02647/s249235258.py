import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, k = geta(int)
    a = tuple(geta(int))

    def update(b):
        r = [0] * n
        for i, bi in enumerate(b):
            i1 = max(0, i - bi)
            i2 = min(n - 1, i + bi)
            r[i1] += 1

            if i2 < n - 1:
                r[i2 + 1] -= 1

        updated = (not r[0] == b[0])
        for i in range(1, n):
            r[i] += r[i - 1]
            if r[i] != b[i]:
                updated = True

        return r, updated

    for i in range(k):
        a, updated = update(a)
        if not updated:
            break

    print(*a, sep=" ")


if __name__ == "__main__":
    main()