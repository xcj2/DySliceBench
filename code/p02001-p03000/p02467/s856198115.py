import math
from typing import List


def calc_divisors(n):
    divisors = [1, n]

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)

    return sorted(divisors)


def prime_factorize(n: int) ->List[int]:
    prime_factors = []
    divisors = calc_divisors(n)[1:]

    for i in divisors:
        while True:
            div, mod = divmod(n, i)
            if mod == 0:
                prime_factors.append(i)
                n = div
            else:
                break
        if n == 1:
            break
    return prime_factors


def main():
    n = int(input())
    prime_factors = prime_factorize(n)
    print("{}: {}".format(n, ' '.join(map(str, prime_factors))))


main()
