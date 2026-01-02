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
    k, n = MI()
    a_list = LI()

    a_list.sort()
    max = 0
    for i, a in enumerate(a_list):
        if i != n - 1:
            d = a_list[i + 1] - a
        else:
            d = a_list[0] + k - a

        if d > max:
            max = d
            max_i = (i + 1) % n

    l = []
    for a in a_list:
        tmp = a - a_list[max_i]
        if tmp >= 0:
            l.append(tmp)
        else:
            l.append(k + tmp)

    l.sort()
    print(l[n - 1])

    pass


if __name__ == "__main__":
    main()
