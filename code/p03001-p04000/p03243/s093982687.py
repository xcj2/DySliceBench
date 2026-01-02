import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N] = string_to_int(inputs[0])
    i = N
    while 1:
        i_str = str(i)
        prev = i_str[0]
        is_ok = True
        for c in i_str:
            if c != prev:
                is_ok = False
                break
        if is_ok:
            return i
        i += 1


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
