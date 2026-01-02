import math
from collections import defaultdict

def is_prime(n: int)-> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    # when n is a prime number
    # x^(n-1) ≡ 1 (mod n)
    return pow(2, (n-1), n) == 1


def prime_factorize(n: int):
    prime_factors = defaultdict(int)

    for i in range(2, int(math.sqrt(n)) + 1):
        if not is_prime(i):
            continue
        while True:
            div, mod = divmod(n, i)
            if mod == 0:
                prime_factors[i] += 1
                n = div
            else:
                break
        if n == 1:
            break
    if n != 1:
        prime_factors[n] = 1

    return prime_factors


def main():
    N, P = map(int, input().split())
    prime_factors = prime_factorize(P)

    gcd = 1
    for k, v in prime_factors.items():
        v_cnt = v // N
        gcd *= pow(k, v_cnt)

    print(gcd)
    return

main()