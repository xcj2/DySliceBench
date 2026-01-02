import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    head = int(inputs[0][:2])
    tail = int(inputs[0][2:])

    if head >= 1 and head <= 12:
        if tail >= 1 and tail <= 12:
            return "AMBIGUOUS"
        else:
            return "MMYY"

    if tail >= 1 and tail <= 12:
        return "YYMM"

    return "NA"


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
