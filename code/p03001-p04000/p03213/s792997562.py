from collections import defaultdict


def calc_divisors_of_factorial(n):
    ret = defaultdict(int)
    for i in range(1, n+1):
        divisors = calc_prime_divisors(i)
        for d in divisors:
            ret[d] += divisors[d]
    return ret


def calc_prime_divisors(n):  # do not contain 1
    ret = defaultdict(int)
    for i in range(2, n+1):
        if is_prime(i):
            while n % i == 0:
                n = n // i
                ret[i] += 1
            if n == 1:
                break
    return ret


def is_prime(n):
    memo = {}
    def calc(n):
        if n in memo:
            return memo[n]
        if n == 1 or n == 2:
            return True
        if n % 2 == 0:
            return False
        d = 3
        while True:
            if d**2 > n:
                break
            if n % d == 0:
                memo[n] = False
                return False
            d += 2
        memo[n] = True
        return True
    return calc(n)


def get_over(divisors, n):
    ret = 0
    for d in divisors:
        if divisors[d]+1 >= n:
            ret += 1
    return ret


def factorial(n):
    memo = {}
    def calc(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return 1
        ret = n *factorial(n-1)
        memo[n] = ret
        return ret
    return calc(n)


def combination(n, k):
    if n <= 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n-k))


def solve(n):
    prime_divisors = calc_divisors_of_factorial(n)
    ret = 0
    over_75 = get_over(prime_divisors, 75)
    over_25 = get_over(prime_divisors, 25)
    over_15 = get_over(prime_divisors, 15)
    over_5 = get_over(prime_divisors, 5)
    over_3 = get_over(prime_divisors, 3)

    if over_75 > 0:
        ret += combination(over_75, 1)
    if over_25 > 0 and over_3-1 > 0:
        ret += combination(over_25, 1) * combination(over_3 - 1, 1)
    if over_15 > 0 and over_5-1 > 0:
        ret += combination(over_15, 1) * combination(over_5 - 1, 1)
    if over_5 > 0 and over_3-2>0:
        ret += combination(over_5, 2) * combination(over_3 - 2, 1)

    return ret


def main():
    N = int(input())
    print(solve(N))


if __name__ == '__main__':
    main()