import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, A, B, C, inputs):
    bamboos = [int(i) for i in inputs]

    def cost(cursor, a, b, c):
        if cursor == N:
            if min(a, b, c) > 0:
                return abs(A-a) + abs(B-b) + abs(C-c) - 30
            else:
                return 1000000000

        t = bamboos[cursor]
        results = []
        results.append(cost(cursor+1, a, b, c))
        results.append(cost(cursor+1, a + t, b, c) + 10)
        results.append(cost(cursor+1, a, b + t, c) + 10)
        results.append(cost(cursor+1, a, b, c + t) + 10)

        return min(results)

    return cost(0, 0, 0, 0)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, A, B, C] = string_to_int(input())
    ret = solve(N, A, B, C, inputs(N))
    print(ret)
