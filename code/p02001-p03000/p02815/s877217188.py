import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N = gete(int)
    c = list(geta(int))
    c.sort(reverse=True)
    mod = 10**9 + 7
    dp = [0] * (N + 1)

    base = 1
    for n in range(1, N + 1):
        dp[n] = (4 * dp[n - 1] + (n + 1) * base * c[n - 1]) % mod
        base = (4 * base) % mod
    print(dp[N])


if __name__ == "__main__":
    main()