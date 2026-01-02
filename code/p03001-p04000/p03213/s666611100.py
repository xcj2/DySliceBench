# ABC114D - 756
from collections import defaultdict


def prime_factorization(x: int) -> dict:
    max_prime, ret = 0, {}
    cnt = 0
    while x % 2 == 0:  # divide x by 2 as much as possible
        x //= 2
        cnt += 1
    if cnt > 0:
        max_prime = 2
        ret[max_prime] = cnt

    cnt = 0
    for i in range(3, int(x ** 0.5) + 1, 2):
        cnt = 0
        while x % i == 0:
            x //= i
            max_prime = i
            cnt += 1
        if cnt > 0:
            ret[max_prime] = cnt

    if x > 2:  # when x is prime greater than 2
        max_prime = x
        ret[max_prime] = 1
    return ret


def count(n: int) -> int:
    return sum(i >= n - 1 for i in prime_factors.values())


def main():
    global prime_factors
    N = int(input())
    prime_factors = defaultdict(int)
    for i in range(2, N + 1):
        for k, v in prime_factorization(i).items():
            prime_factors[k] += v
    ans = (
        count(75)
        + count(25) * (count(3) - 1)
        + count(15) * (count(5) - 1)
        + count(5) * (count(5) - 1) * (count(3) - 2) // 2
    )
    print(ans)


if __name__ == "__main__":
    main()