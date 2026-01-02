import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def bfs(N):
    q = deque(["7", "5", "3"])
    res = []

    while q:
        s = q.popleft()

        for c in ["7", "5", "3"]:
            new = s + c

            if int(new) > N:
                continue

            if "7" in new and "5" in new and "3" in new:
                res.append(new)

            q.append(new)

    return len(res)


def main():
    N = int(input())

    ans = bfs(N)
    print(ans)


if __name__ == "__main__":
    main()
