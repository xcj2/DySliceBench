import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def solve(N):
    M = 3501

    for h in range(1, M):
        for n in range(h, M):
            denominator = 4 * n * h - N * h - N * n
            if denominator <= 0:
                continue
            numerator = N * h * n

            if numerator % denominator == 0:
                return h, n, numerator // denominator


def main():
    N = int(input())
    h, n, w = solve(N)
    print(h, n, w)


if __name__ == "__main__":
    main()
