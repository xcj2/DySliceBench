import fractions
import sys
from functools import reduce

input = sys.stdin.readline


def main():
    n, m = input_list()
    if n >= m // 2:
        print(m//2)
    else:
        c = (m-(2*n))//4
        print(n+c)


def input_list():
    return list(map(int, input().split()))


def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


def gcd(*numbers):
    return reduce(fractions.gcd, numbers)


def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)


if __name__ == "__main__":
    main()
