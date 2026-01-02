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


def LIN(n: int):
    return [I() for _ in range(n)]


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    h, w = MI()
    s = [["."] + list(input().rstrip()) + ["."] for _ in range(h)]

    empty = ["."] * (w + 2)
    s.append(empty)
    s.insert(0, empty)
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if s[i][j] == "#":
                continue
            else:
                bomb = 0
                for row in [-1, 0, 1]:
                    for col in [-1, 0, 1]:
                        if s[i + row][j + col] == "#":
                            bomb += 1
                s[i][j] = str(bomb)
        print("".join(s[i][1 : w + 1]))

    pass


if __name__ == "__main__":
    main()
