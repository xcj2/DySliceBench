import fractions
import sys
from functools import reduce
import math

input = sys.stdin.readline


def main():
    n = int(input())
    h = input_list()
    count = 0
    while list(set(h)) != [0]:
        count += 1
        flag = False
        for i, v in enumerate(h):
            if v != 0:
                flag = True
                h[i] -= 1
            else:
                if flag:
                    break
    print(count)

def divide_two(n):
    c = 0
    while True:
        if c >= 2:
            break
        if n % 2 != 0:
            break
        n //= 2
        c += 1
    return c

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
