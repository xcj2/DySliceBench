import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a > b:
        return gcd(b, a % b)
    else:
        return gcd(a, b % a)


def gcd_multi(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    ret = gcd(nums.pop(), nums.pop())
    while len(nums) > 0:
        ret = gcd(ret, nums.pop())
    return ret


def solve(inputs):
    [S] = string_to_int(inputs[0])
    current = S
    appeared_set = {current}
    i = 1
    while 1:
        i += 1
        if current % 2 == 0:
            current /= 2
        else:
            current = 3 * current + 1

        if current in appeared_set:
            return i

        appeared_set.add(current)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
