import sys
from collections import deque
from functools import reduce
import copy


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    nums = string_to_int(inputs[0])
    N = len(nums)
    for i in range(N):
        nums[i] -= (i+1)
    nums.sort()
    total = reduce(lambda x, y: x + y, nums, 0)
    half = N // 2
    sub = nums[half]
    total = reduce(lambda acc, x: acc + abs(x - sub), nums, 0)
    return total


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)