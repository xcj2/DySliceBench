import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    cities = list(map(string_to_int, inputs))
    prefecutures = {}
    for i, c in enumerate(cities):
        p = c[0]
        y = c[1]
        if p not in prefecutures:
            prefecutures[p] = []
        prefecutures[p].append((i, p, y))

    ids = {}
    for p in prefecutures.keys():
        prefecutures[p].sort(key=lambda x: x[2])
        for order, c in enumerate(prefecutures[p]):
            [ic, pc, yc] = c
            ids[ic] = "{:06d}{:06d}".format(p, order+1)

    ret = ""
    for i in range(0, M):
        ret += ids[i] + "\n"

    return ret.strip()


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)