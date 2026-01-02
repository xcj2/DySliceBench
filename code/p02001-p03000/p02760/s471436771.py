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
    A = []
    for _ in range(3):
        a = read_list()
        A.extend(a)
    N = int(input())
    B = [False] * 9
    for _ in range(N):
        b = int(input())
        if b in A:
            c = A.index(b)
            B[c] = True

    if ((B[0] and B[1] and B[2]) or
        (B[3] and B[4] and B[5]) or
        (B[6] and B[7] and B[8]) or 
        (B[0] and B[3] and B[6]) or
        (B[1] and B[4] and B[7]) or
        (B[2] and B[5] and B[8]) or
        (B[0] and B[4] and B[8]) or
        (B[2] and B[4] and B[6])):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()