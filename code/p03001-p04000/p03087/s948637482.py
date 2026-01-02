import fractions
import sys
from functools import reduce
import math

input = sys.stdin.readline


def main():
    n, q = input_list()
    s = input()
    cumulative_sum = [0]
    i = 0
    for index, sv in enumerate(s):
        if index >= len(s)-1:
            continue
        if s[index] + s[index+1] == 'AC':
            i += 1
            cumulative_sum.append(i)
        else:
            cumulative_sum.append(i)
    for _ in range(q):
        l, r = input_list()
        print(cumulative_sum[r-1] - cumulative_sum[l-1])


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
