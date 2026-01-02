import fractions
import sys
from functools import reduce
import math

input = sys.stdin.readline

def main():
    n, m = input_list()
    if n >= m:
        print(0)
        exit(0)
    x = list(sorted(input_list()))
    diffs = []
    for i in range(1, m):
        a = abs(x[i] - x[i-1])
        diffs.append((i, a))
    dd = list(sorted(diffs, key=lambda v: v[1], reverse=True))
    ans = 0
    for i, v in enumerate(dd):
        if i < n-1:
            continue
        ans += v[1]
    print(ans)
    # args = [d[0] for d in dd[:n-1]]
    # r = divide_list(x, args)
    # ans = 0
    # for xx in r:
    #     ans += max(xx) - min(xx)
    # print(ans)


def divide_list(l, args):
    result = []
    pre = 0
    for i, a in enumerate(args):
        if i != 0:
            pre = args[i-1]
        result.append(l[pre:a])
        if i == len(args) - 1:
            result.append(l[a:])
    return result

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
