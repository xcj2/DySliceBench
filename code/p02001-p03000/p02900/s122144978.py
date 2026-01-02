# ABC142D - Disjoint Set of Common Divisors
def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


def prime_factorization(x: int) -> dict:
    max_prime, ret = 0, {}

    # Divide x by 2 as much as possible
    cnt = 0
    while x % 2 == 0:
        x //= 2
        cnt += 1
    if cnt > 0:
        max_prime = 2
        ret[max_prime] = cnt

    # x must be odd -> skip even numbers
    cnt = 0
    for i in range(3, int(x ** 0.5) + 1, 2):
        cnt = 0
        while x % i == 0:
            x //= i
            max_prime = i
            cnt += 1
        if cnt > 0:
            ret[max_prime] = cnt

    if x > 2:  # To handle the case when x is prime greater than 2
        max_prime = x
        ret[max_prime] = 1
    return ret


def main():
    # compute the number of common prime factors
    A, B = map(int, input().split())
    g = gcd(A, B)
    ans = len(prime_factorization(g).keys()) + 1
    print(ans)


if __name__ == "__main__":
    main()