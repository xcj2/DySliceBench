import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


MOD = 10 ** 9 + 7


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    C = [0] * N

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        # divisors.sort()
        return divisors

    for i in range(N):
        if A[N - i - 1] == 1:
            if C[N - i - 1] == 0:
                B.append(N - i)
                D = make_divisors(N - i)
                for d in D:
                    C[d - 1] += 1
                    C[d - 1] %= 2
        else:
            if C[N - i - 1] == 1:
                B.append(N - i)
                D = make_divisors(N - i)
                for d in D:
                    C[d - 1] += 1
                    C[d - 1] %= 2
    print(len(B))
    print(*B, sep=" ")


if __name__ == "__main__":
    main()
