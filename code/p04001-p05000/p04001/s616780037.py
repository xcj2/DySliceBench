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
    s = input().rstrip()

    n = len(s) - 1
    ans = 0
    for i in range(2 ** n):
        tmp = 0
        for j in range(n):
            if (i >> j) & 1:
                ans += int(s[tmp : j + 1])
                tmp = j + 1
        ans += int(s[tmp:])

    print(ans)


if __name__ == "__main__":
    main()
