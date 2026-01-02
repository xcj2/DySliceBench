import sys
from collections import deque
import copy

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    T = inputs[1]

    string_queue = deque(S)
    T_queue = deque(T)

    for i in range(len(S)):
        if string_queue == T_queue:
            return 'Yes'
        p = string_queue.pop()
        string_queue.appendleft(p)
    return 'No'


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
