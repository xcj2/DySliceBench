import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N, M = map(int, input().split())

    def make_divisors(n):
        divisors = []
        cnt = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        divisors.sort()
        return divisors

    divisor = make_divisors(M)
    cnt = len(divisor)
    for i in range(cnt):
        if M // divisor[cnt - i - 1] >= N:
            print(divisor[cnt - i - 1])
            return


if __name__ == "__main__":
    main()
