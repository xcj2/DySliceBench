import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, T, inputs):
    routes = list(map(string_to_int, inputs))
    min_cost = -1
    for r in routes:
        if r[1] <= T and (min_cost == -1 or r[0] < min_cost):
            min_cost = r[0]
    if min_cost == -1:
        return "TLE"
    return str(min_cost)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, T] = string_to_int(input())
    ret = solve(N, T, inputs(N))
    print(ret)
