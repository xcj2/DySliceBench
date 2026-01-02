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
    abcd = input().rstrip()

    op = [""] * 3
    for i in range(2 ** 3):
        r = int(abcd[0])
        for j in range(3):
            if (i >> j) & 1:
                r += int(abcd[j + 1])
                op[j] = "+"
            else:
                r -= int(abcd[j + 1])
                op[j] = "-"
        if r == 7:
            ans = abcd[0]
            for j in range(3):
                ans += op[j] + abcd[j + 1]
            ans += "=7"
            print(ans)
            exit()


if __name__ == "__main__":
    main()
