import math


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    f(K) = number of divisors of K
    sum(K*f(K)), K=1...N
    f(1) = 1, f(2) = 2, f(3) = 2, f(4) = 3
    1 <= N <= 10**7

    36 = 1, 2, 3, 4, 6, 9, 12, 18, 36
    f(36) = 9
    """
    N = read_int()
    counter = [1]*(N+1)
    for divisor in range(2, N+1):
        for step in range(divisor, N+1, divisor):
            counter[step] += 1
    return sum(k*counter[k] for k in range(1, N+1))


if __name__ == '__main__':
    print(solve())
