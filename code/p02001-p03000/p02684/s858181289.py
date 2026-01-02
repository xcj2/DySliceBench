import sys
from math import sqrt
from collections import Counter, defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


def LIN(n: int):
    return [I() for _ in range(n)]


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    n, k = MI()
    al = LI()

    al.insert(0, 0)
    now = 1
    if n >= k:
        for _ in range(k):
            now = al[now]
    else:
        passed = [-1] * (n + 1)
        i = 0
        while passed[now] == -1:
            passed[now] = i
            now = al[now]
            i += 1

        loop = i - passed[now]

        for _ in range((k - passed[now]) % loop):
            now = al[now]

    print(now)


if __name__ == "__main__":
    main()
