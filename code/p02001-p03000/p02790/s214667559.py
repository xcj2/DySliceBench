import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7


def read_values():
    return map(int, input().split())


def read_index():
    return map(lambda x: x - 1, map(int, input().split()))


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def functional(N, mod):
    F = [1] * (N + 1)
    for i in range(N):
        F[i + 1] = (i + 1) * F[i] % mod
    return F


def main():
    a, b = read_values()
    print(str(min(a, b)) * max(a, b))


if __name__ == "__main__":
    main()