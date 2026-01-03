import sys
from functools import reduce
import copy
import math
from pprint import pprint
import collections
import bisect


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def int_inputs(num_of_input):
    ins = [int(input()) for i in range(num_of_input)]
    return ins


def solve(inputs):
    [H, W] = string_to_int(inputs[0])
    IDEAL_SIZE = H * W / 3

    def separate_first(SH, SW):
        most_closed_size = None
        most_closed_i = None
        for h in range(1, SH):
            tmp_size = h * SW
            if most_closed_size is None:
                most_closed_size = tmp_size
                most_closed_i = h
            else:
                most_closed_diff = abs(IDEAL_SIZE - most_closed_size)
                tmp_diff = abs(IDEAL_SIZE - tmp_size)

                if most_closed_diff > tmp_diff:
                    most_closed_size = tmp_size
                    most_closed_i = h

        return (most_closed_i, most_closed_size)

    def separate_second_row(start_h, SH, SW):
        second_i = (SH - start_h) // 2 + start_h
        second_s = (second_i - start_h) * SW
        third_s = (SH - second_i) * SW
        return (second_i, second_s, third_s)

    def separate_second_column(start_h, SH, SW):
        second_i = SW // 2
        second_s = (SH - start_h) * second_i
        third_s = (SH - start_h) * (SW - second_i)
        return (second_i, second_s, third_s)

    def max_diff(f_s, s_s, t_s):
        diff_s = []
        diff_s.append(abs(f_s - s_s))
        diff_s.append(abs(f_s - t_s))
        diff_s.append(abs(s_s - t_s))

        return max(diff_s)

    diffs = []
    if H == 1:
        f_i, f_s = separate_first(W, H)
        s_i, s_s, t_s = separate_second_row(f_i, W, H)
        diffs.append(max_diff(f_s, s_s, t_s))
    elif W == 1:
        f_i, f_s = separate_first(W, H)
        s_i, s_s, t_s = separate_second_row(f_i, W, H)
        diffs.append(max_diff(f_s, s_s, t_s))
    else:
        f_i, f_s = separate_first(H, W)
        s_i, s_s, t_s = separate_second_row(f_i, H, W)
        diffs.append(max_diff(f_s, s_s, t_s))

        f_i, f_s = separate_first(W, H)
        s_i, s_s, t_s = separate_second_row(f_i, W, H)
        diffs.append(max_diff(f_s, s_s, t_s))

        f_i, f_s = separate_first(H, W)
        s_i, s_s, t_s = separate_second_column(f_i, H, W)
        diffs.append(max_diff(f_s, s_s, t_s))

        f_i, f_s = separate_first(W, H)
        s_i, s_s, t_s = separate_second_column(f_i, W, H)
        diffs.append(max_diff(f_s, s_s, t_s))
    return min(diffs)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
