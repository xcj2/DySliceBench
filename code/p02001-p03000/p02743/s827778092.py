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
    a, b, c = read_values()
    r = c - a - b
    if r <= 0:
        print("No")
        return
    
    print("Yes" if (c - a - b) ** 2 > 4 * a * b else "No")

if __name__ == "__main__":
    main()