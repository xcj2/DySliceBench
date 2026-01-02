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
    n = I()
    s = input().rstrip()

    r = [i for i, x in enumerate(s) if x == "R"]
    b = [i for i, x in enumerate(s) if x == "B"]
    g = [i for i, x in enumerate(s) if x == "G"]

    c = 0
    for d in range(1, int((n - 3) / 2) + 2):
        for i in range(n):
            tmp = i + d * 2
            if tmp == n:
                break
            if s[i] != s[i + d] and s[i + d] != s[tmp] and s[i] != s[tmp]:
                c += 1

    print(len(r) * len(b) * len(g) - c)


if __name__ == "__main__":
    main()
