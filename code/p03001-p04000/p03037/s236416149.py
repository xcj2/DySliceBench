import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(num_card, num_gate, inputs):
    gate_card = list(map(lambda x: string_to_int(x), inputs))
    min_card = 1
    max_card = num_card
    for d in gate_card:
        if d[0] > min_card:
            min_card = d[0]
        if d[1] < max_card:
            max_card = d[1]

    if max_card - min_card >= 0:
        return max_card - min_card + 1
    return 0


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(M))
    print(ret)
