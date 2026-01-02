import sys
import math

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


# def factorization(n):
#     factor = []
#     tmp = int(math.sqrt(n)) + 1
#     for i in range(2, tmp):
#         while n % i == 0:
#             n //= i
#             factor.append(i)
#         if len(factor) != 0:
#             factor.append(n)
#             return factor
#     return []


def solve(inputs):
    N = int(inputs[0])
    # factors = factorization(N)
    min_diff = None
    for i in range(1, 1000001):
        if N % i == 0:
            a = N // i
            diff = a + i - 2
            if min_diff is None or min_diff > diff:
                min_diff = diff
    return min_diff


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
