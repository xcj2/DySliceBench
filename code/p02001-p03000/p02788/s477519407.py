import sys
from collections import defaultdict
from queue import deque

readline = sys.stdin.buffer.readline


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


sys.setrecursionlimit(10**5)


def main():
    n, d, a = geta(int)
    mon = []
    ans = 0

    for _ in range(n):
        x, h = geta(int)
        mon.append([x, (h + a - 1) // a])

    mon.sort()

    bom = deque()
    cur = 0
    for i, mi in enumerate(mon):

        while len(bom) != 0 and bom[0][0] < mi[0]:
            b = bom.popleft()
            cur -= b[1]

        if mi[1] <= cur:
            continue
        else:
            b1 = mi[1] - cur
            bom.append((mi[0] + 2 * d, b1))
            cur += b1
            ans += b1

    print(ans)


if __name__ == "__main__":
    main()