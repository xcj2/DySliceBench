import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(H, W, inputs):
    delete_row = []
    i = 0
    while len(inputs) != 0 and i < len(inputs):
        is_all_white = True
        for c in inputs[i]:
            is_all_white = is_all_white and c == '.'
        if is_all_white:
            inputs.pop(i)
        else:
            i += 1
    blank_columns = {i for i in range(len(inputs[0]))}
    for row in inputs:
        for i, c in enumerate(row):
            if c != '.' and i in blank_columns:
                blank_columns.remove(i)
    for row in inputs:
        for i, c in enumerate(row):
            if i not in blank_columns:
                print(c, end='')
        print('')

    # return inputs


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [H, W] = string_to_int(input())
    ret = solve(H, W, inputs(H))
    # print(ret)
