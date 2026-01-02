import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**5)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n = gete(int)
    t = [[]]
    for _ in range(n):
        ret = []
        for _ in range(gete(int)):
            ret.append(tuple(geta(int)))
        t.append(ret)

    ans = 0
    for c in range(2**n):
        l = [0] * (n + 1)

        cur = 1
        tmp = c
        while tmp > 0:
            if tmp & 1 == 1:
                l[cur] = 1
            cur += 1
            tmp = tmp >> 1

        ok = True
        for i, h in enumerate(l):
            if h == 1:
                for tj in t[i]:
                    if tj[1] != l[tj[0]]:
                        ok = False
                        break
            if not ok:
                break

        if ok:
            ans = max(ans, sum(l))

    print(ans)


if __name__ == "__main__":
    main()