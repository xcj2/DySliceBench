import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    count = 0
    for i in range(1, N + 1):
        divisor_num = 0
        if i % 2 == 0:
            continue
        for j in range(1, i + 1):
            if i % j == 0:
                divisor_num += 1
        if divisor_num == 8:
            count += 1
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
