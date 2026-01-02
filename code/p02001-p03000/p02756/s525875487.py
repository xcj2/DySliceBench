import collections
import math
import operator as op
from functools import reduce
from collections import Counter
import numpy as np
import math
import bisect
import heapq


MOD = 1000000007


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def get_inputs(cast_func=None):
    if cast_func is None:
        return input().split()
    else:
        return list(map(cast_func, input().split()))


def get_input(cast_func=None):
    if cast_func is None:
        return input()
    else:
        return cast_func(input())


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def main():
    S = get_input()
    Q = get_input(int)

    # NOTE: need to reverse
    heads = ""
    tails = ""
    direction = 1
    for _ in range(Q):
        query = get_input()
        if query[0] == "1":
            direction *= -1
        else:
            _, F, C = query.split(" ")
            if F == "1":
                if direction == 1:
                    heads += C
                else:
                    tails += C
            else:
                if direction == 1:
                    tails += C
                else:
                    heads += C
     
    if direction == 1:
        print(heads[::-1] + S + tails)
    else:
        print(tails[::-1] + S[::-1] + heads)


if __name__ == '__main__':
    main()
