import sys
from collections import deque
import copy

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    nums = string_to_int(inputs[0])
    count = nums[0]
    for i in range(1, len(nums)):
        count *= nums[i]
    count -= 1
    ret = 0
    for n in nums:
        ret += count % n
    return ret


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
