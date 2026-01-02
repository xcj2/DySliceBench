import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(100000)


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
    N, M = read_values()
    F = read_lists(M)
    r = range(10) if N == 1 else (range(10, 100) if N == 2 else range(100, 1000))
    for i in r:
        if all(str(i)[f[0] - 1] == str(f[1]) for f in F):
            print(i)
            return
    print(-1)


if __name__ == "__main__":
    main()