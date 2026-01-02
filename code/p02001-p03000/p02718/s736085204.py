import sys
from math import sqrt
from collections import Counter, defaultdict

input = sys.stdin.readline


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
    n, m = MI()
    a_list = LI()
    c = 0
    votes = sum(a_list)
    for a in a_list:
        if a >= votes / (4 * m):
            c += 1

    if c < m:
        print("No")
    else:
        print("Yes")
    pass


if __name__ == "__main__":
    main()
