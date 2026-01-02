import fractions
import sys
from functools import reduce
import math

input = sys.stdin.readline


def main():
    r, g, b, n = input_list()
    ans = 0
    for x in range(n+1):
        for y in range(n+1):
            z = n - (x*r) - (y*g)
            if z < 0:
                continue
            if z % b != 0:
                continue
            ans += 1
    print(ans)


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
