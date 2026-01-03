import fractions
import sys
from functools import reduce
import math

input = sys.stdin.readline


def main():
    n = int(input())
    a = input_list()
    if list(set(a)) == [1]:
        print('No')
        exit()

    divide_counters = []
    for v in a:
        dt = divide_two(v)
        if dt == 0:
            divide_counters.append(1)
        elif dt == 1:
            divide_counters.append(2)
        else:
            divide_counters.append(4)
    
    if set(divide_counters) == {1, 4}:
        if divide_counters.count(1) <= divide_counters.count(4) + 1:
            print('Yes')
            exit()
        else:
            print('No')
            exit()
    if divide_counters.count(1) <= divide_counters.count(4):
        print('Yes')
    else:
        print('No')
        
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
