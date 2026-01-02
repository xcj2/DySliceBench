import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def _euclid(x, y):
    if x > y:
        large = x
        small = y
    else:
        large = y
        small = x

    if small == 0:
        return large

    return _euclid(small, large % small)


def euclid_multi(nums):
    if len(nums) == 1:
        return nums[0]

    e = -1
    for i in range(1, len(nums)):
        if e == -1:
            e = _euclid(nums[0], nums[1])
        else:
            e = _euclid(e, nums[i])
    return e


def solve(inputs):
    [x1, y1, x2, y2] = string_to_int(inputs[0])
    diff_x = x2 - x1
    diff_y = y2 - y1
    x3 = x2 - diff_y
    y3 = y2 + diff_x
    x4 = x1 - diff_y
    y4 = y1 + diff_x
    return "{} {} {} {}".format(x3, y3, x4, y4)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
