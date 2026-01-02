import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def bfs(N):
    q = deque(["a"])

    res = []
    while q:
        s = q.popleft()
        if len(s) == N:
            res.append(s)
            continue

        n = len(set(list(s)))
        for i in range(n + 1):
            c = chr(ord("a") + i)
            q.append(s + c)

    return res


def main():
    N = int(input())
    ans = bfs(N)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
