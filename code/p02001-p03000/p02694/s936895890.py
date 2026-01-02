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
    x = I()

    a = 100
    i = 0
    while True:
        a = int(a * 1.01)
        i += 1
        if a >= x:
            print(i)
            exit()


if __name__ == "__main__":
    main()
