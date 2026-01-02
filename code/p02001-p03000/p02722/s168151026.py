import sys
from math import sqrt
from collections import Counter, defaultdict, deque

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


def devisor(n):
    ret = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ret.append(i)
            if n // i != i:
                ret.append(n // i)
    return ret


def main():
    n = I()

    divs1 = devisor(n)
    divs2 = devisor(n - 1)
    c = len(divs2) - 1
    for val in divs1:
        if val != 1:
            tmp = n
            while tmp % val == 0:
                tmp = tmp // val
            if tmp % val == 1:
                c += 1
    print(c)


if __name__ == "__main__":
    main()

