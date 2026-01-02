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
    print(
        "APPROVED"
        if all(map(lambda a: a % 2 == 1 or (a % 3 == 0 or a % 5 == 0), A))
        else "DENIED"
    )


if __name__ == "__main__":
    main()
