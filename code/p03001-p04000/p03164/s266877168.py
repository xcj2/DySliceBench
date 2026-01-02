import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, W = geta(int)
    INF = 10 << 60
    VMAX = 10**5
    cur = [INF] * (VMAX + 1)
    cur[0] = 0

    for i in range(N):
        w, v = geta(int)
        update = cur[:]

        for j in range(v, VMAX + 1):
            if cur[j - v] == INF: continue
            tmp = cur[j - v] + w
            if tmp < cur[j]: update[j] = tmp

        cur = update

    ans = 0
    for v in range(VMAX + 1):
        if cur[v] <= W: ans = v
    print(ans)


if __name__ == "__main__":
    main()
