import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def make_divisors(n):
    # exclude itself
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N)
    B = []
    for i in range(N - 1, -1, -1):
        S[i] %= 2
        if A[i] != S[i]:
            S[i] += 1
            B.append(i + 1)
            ds = make_divisors(i + 1)
            for d in ds:
                S[d - 1] += 1
        else:
            continue

    print(len(B))
    print(*B, sep=" ")


if __name__ == "__main__":
    main()
