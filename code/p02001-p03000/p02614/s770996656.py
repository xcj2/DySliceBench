import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    h, w, k = geta(int)
    c = []
    for _ in range(h):
        c.append(gete())

    ans = 0
    for bi in range(1 << h):
        for bj in range(1 << w):

            rem = 0
            for i in range(h):
                if bi >> i & 1 == 1:
                    continue
                for j in range(w):
                    if bj >> j & 1 == 1:
                        continue
                    if c[i][j] == "#":
                        rem += 1

            if rem == k:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
