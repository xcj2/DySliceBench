from math import floor
from collections import defaultdict


def Calc_Divisors(num):
    divisors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
    # divisors.sort()
    return divisors


def main():
    N = int(input())
    divlist = defaultdict(int)

    ans = 0
    for i in range(1, N+1):
        ans += i/2 * floor(N/i) * floor(1+N/i)

    print(int(ans))


def test():
    ans = 0
    for i in range(1, 10000000):
        d = Calc_Divisors(i)
        print(len(d))
        ans += len(d) * i
        print(ans)


if __name__ == "__main__":
    main()
