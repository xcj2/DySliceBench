import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, D] = string_to_int(inputs[0])
    counter = -D
    num_person = 0
    is_just_increase = False
    for i in range(N):
        is_just_increase = False
        if counter == D:
            counter = -D
            num_person += 1
            is_just_increase = True
        else:
            counter += 1
    if not is_just_increase:
        num_person += 1
    return num_person


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
