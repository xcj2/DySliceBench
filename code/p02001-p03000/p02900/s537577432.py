# ABC142D - Disjoint Set of Common Divisors
def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x


def prime_factors(x: int) -> list:
    if x % 2:
        max_prime, factors = 0, []
    else:
        max_prime, factors = 2, [2]
        while x % 2 == 0:
            x //= 2
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            factors.append(i)
            while x % i == 0:
                x //= i
    if x > 2:  # when x is prime greater than 2
        factors.append(x)
    return factors


def main():
    # compute the number of prime factors of gcd(A, B)
    A, B = map(int, input().split())
    g = gcd(A, B)
    ans = len(prime_factors(g)) + 1
    print(ans)


if __name__ == "__main__":
    main()
