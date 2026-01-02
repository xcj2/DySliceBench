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


def main():
    k = I()

    q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(1, 10 ** 5 + 1):
        ln = q.popleft()

        if i == k:
            print(ln)
            break

        r = ln % 10
        new_ln = ln * 10 + r
        if r != 0:
            q.append(new_ln - 1)
        q.append(new_ln)
        if r != 9:
            q.append(new_ln + 1)


if __name__ == "__main__":
    main()
