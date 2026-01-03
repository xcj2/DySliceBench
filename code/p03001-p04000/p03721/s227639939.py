import fractions
import sys
from functools import reduce
import collections
import time
input = sys.stdin.readline


def main():
    n, k = input_list()
    total = 0
    a_map = {}
    for _ in range(n):
        num, count = input_list()
        if num in a_map:
            a_map[num] += count
        else:
            a_map[num] = count
    sa_map = sorted(a_map.items(), key=lambda x: x[0])

    for num, count in sa_map:
        total += count
        if k <= total:
            print(num)
            break
    # 2 3 3 3 4 4 4

def get_camulative(l):
    import itertools
    # 累積和
    return [0] + list(itertools.accumulate(l))


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
