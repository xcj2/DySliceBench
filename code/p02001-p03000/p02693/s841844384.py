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
    k = I()
    a, b = MI()

    for i in range(a, b + 1):
        if i % k == 0:
            print("OK")
            exit()

    print("NG")


if __name__ == "__main__":
    main()
