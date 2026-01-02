# from math import sqrt
# from heapq import heappush, heappop
# from collections import deque
from functools import reduce

# a, b = [int(v) for v in input().split()]


def main():
    N, M = [int(v) for v in input().split()]
    A = list(set([int(v) // 2 for v in input().split()]))

    def func(a):
        count = 0
        while a % 2 == 0:
            count += 1
            a //= 2
        return count

    fa = func(A[0])
    for a in A[1:]:
        if func(a) != fa:
            print(0)
            exit()

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(v1, v2):
        return v1 * v2 // gcd(v1, v2)

    a_lcm = 1
    for a in A:
        d = gcd(a_lcm, a)
        a_lcm = a_lcm * a // d
        if a_lcm > M:
            print(0)
            exit()

    # a_lcm = reduce(lambda v1, v2: lcm(v1, v2), A)

    print((M // a_lcm + 1) // 2)


main()
