# from math import sqrt
# from heapq import heappush, heappop
# from collections import deque
from functools import reduce

# a, b = [int(v) for v in input().split()]


def main():
    N, M = map(int, input().split())
    A = [int(v) // 2 for v in input().split()]

    def gcd(v1, v2):
        v = v1 % v2
        if v == 0:
            return v2
        return gcd(v2, v)

    def lcm(v1, v2):
        return v1 * v2 // gcd(v1, v2)

    lcma = reduce(lcm, A)

    if next(filter(lambda v: (lcma // v) % 2 == 0, A), None) is not None:
        print(0)
        exit()

    print((M + lcma) // (2 * lcma))


main()
