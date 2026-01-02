import sys
from math import sqrt
from collections import Counter

input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    _ = I()
    a_list = input().split()

    c = Counter(a_list)
    n = {}
    t = 0
    for k, v in c.items():
        n[k] = v - 1
        if v >= 2:
            t += int(v * (v - 1) / 2)

    for a in a_list:
        print(t - n[a])
    pass


if __name__ == "__main__":
    main()
