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
    [N, X] = string_to_int(inputs[0])
    x = string_to_int(inputs[1])
    x.append(X)
    x.sort()
    diffs = []
    for i in range(len(x)-1):
        diffs.append(x[i+1] - x[i])

    e = euclid_multi(diffs)
    return e


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
