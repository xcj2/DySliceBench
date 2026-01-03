import fractions
import sys
from functools import reduce
import math

input = sys.stdin.readline


def main():
    n, a, b = input_list()
    if a > b:
        print(0)
        exit(0)
    if n == 1 and a != b:
        print(0)
        exit(0)
    if n == 1 and a == b:
        print(1)
        exit(0)
    min_num = (a*(n-1))+b
    max_num = (b*(n-1))+a
    print(max_num-min_num+1)


def get_camulative(l):
    import itertools
    # 累積和
    return [0] + list(itertools.accumulate(l))

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


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
