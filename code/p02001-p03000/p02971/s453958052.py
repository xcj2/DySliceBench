import sys
from collections import deque
import copy

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    A = list(map(int, inputs))
    B = copy.copy(A)
    B.sort()
    first_num = B[-1]
    second_num = B[-2]
    ret = ''
    for a in A:
        if a == first_num:
            ret += str(second_num) + '\n'
        else:
            ret += str(first_num) + '\n'
    return ret.strip()


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
