import sys
import math
from collections import Counter, defaultdict, deque
from functools import reduce

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

    def gcd(a, b, c):
        return math.gcd(math.gcd(a, b), c)

    sum = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            for c in range(1, k + 1):
                sum += gcd(a, b, c)

    print(sum)


if __name__ == "__main__":
    main()
