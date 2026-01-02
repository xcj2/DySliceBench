import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    elif a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def gcd_m(*args):
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]
    if len(args) >= 2:
        ret = gcd(args[0], args[1])

    for value in args[2:]:
        ret = gcd(ret, value)
    return ret


def solve(inputs):
    [N] = string_to_int(inputs[0])
    # A = [0] + (string_to_int(inputs[1])) + [0]
    A = string_to_int(inputs[1])

    if N == 2:
        return max(A)

    left_gcd_memo = deque([0])
    right_gcd_memo = deque([0])

    for v in A:
        left_gcd_memo.append(gcd(left_gcd_memo[-1], v))
    left_gcd_memo.append(0)
    for v in reversed(A):
        right_gcd_memo.appendleft(gcd(right_gcd_memo[0], v))
    right_gcd_memo.appendleft(0)

    max_gcd = 0
    for i in range(0, len(A)):
        left = left_gcd_memo[i]
        right = right_gcd_memo[i+2]
        g = gcd(left_gcd_memo[i], right_gcd_memo[i+2])
        max_gcd = g if g > max_gcd else max_gcd

    return max_gcd


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
