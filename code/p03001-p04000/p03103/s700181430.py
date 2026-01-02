import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    stores = [string_to_int(i) for i in inputs]
    wants = M
    money = 0
    for price, num in sorted(stores, key=lambda i: i[0]):
        if wants > num:
            money += price * num
            wants -= num
        else:
            money += price * wants
            break

    return money


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(N))
    print(ret)
