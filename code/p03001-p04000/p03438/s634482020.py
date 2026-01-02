import bisect
import heapq
import sys
import queue


input = sys.stdin.readline
sys.setrecursionlimit(100000)


class V:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)

    def get(self):
        return self.v


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    N = int(input())
    A = read_list()
    B = read_list()

    KA = 0
    KB = 0
    for a, b in zip(A, B):
        if a == b:
            continue

        if a > b:
            KB += a - b
            continue

        if a % 2 != b % 2:
            KB += 1
            b += 1

        KA += (b - a) // 2

    print("Yes" if KA >= KB else "No")


if __name__ == "__main__":
    main()
