import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N = int(input())
    if N < 105:
        print(0)
        return

    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors

    cnt = 1
    for n in range(106, N + 1):
        if n % 2 == 1:
            d = make_divisors(n)
            if len(d) == 8:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
