from collections import defaultdict
from itertools import product, groupby
from math import pi
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = 10 ** 10


# aとbの最大公約数
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# aとbの最小公倍数
def lcm(a, b):
    g = gcd(a, b)
    return a // g * b


def main():
    N = int(input())
    t_list = list(sorted([int(input()) for _ in range(N)]))
    ans = 1
    for t in t_list:
        ans = lcm(ans, t)

    print(ans)

if __name__ == '__main__':
    main()
