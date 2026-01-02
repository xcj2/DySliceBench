import collections
import fractions
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = input_list()
    ac = collections.Counter(a)
    # 個数が少ない場合は空にする
    ans = 0
    for num, count in ac.items():
        if num < count:
            ans += count - num
        if num > count:
            ans += count
    print(ans)

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
