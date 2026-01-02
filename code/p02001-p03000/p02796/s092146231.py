import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def f(A):
    min_num = A[0] + A[-1]


def main():
    N = int(input())
    R = []
    for _ in range(N):
        X, L = map(int, input().split())
        R.append((X - L, X + L))
    
    R.sort(key=lambda l: l[1])

    res = 0
    T = None    
    for r in R:
        if T is None or r[0] >= T:
            T = r[1]
            res += 1

    print(res)


if __name__ == "__main__":
    main()
