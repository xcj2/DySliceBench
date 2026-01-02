import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort(reverse=True)
    return divisors


def main():
    N, M = map(int, input().split())

    divisors = make_divisors(M)
    ans = 1
    for d in divisors:
        if M // d >= N:
            if ans < d:
                ans = d

    print(ans)


if __name__ == "__main__":
    main()
