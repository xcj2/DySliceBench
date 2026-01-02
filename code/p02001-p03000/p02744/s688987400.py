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


def add(S):
    S2 = []
    for n, s in S:
        for m in range(0, n + 1):
            w = chr(ord("a") + m)
            if m == n:
                S2.append((n + 1, s + w))
            else:
                S2.append((n, s + w))
    return S2


def main():
    N = int(input())

    S = [(0, "")]
    for _ in range(N):
        S = add(S)
    
    for _, s in S:
        print(s)
    

if __name__ == "__main__":
    main()