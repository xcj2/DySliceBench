import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n = gete(int)
    a = tuple(geta(int))
    s = sum(a)

    cur = 1
    ans = 0

    for ai in a:
        if cur < ai:
            print(-1)
            exit()
        else:
            ans += min(cur, s)
            cur = 2 * (min(cur, s) - ai)
            s -= ai

    print(ans)


if __name__ == "__main__":
    main()