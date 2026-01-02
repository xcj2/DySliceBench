import sys
import math

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N] = string_to_int(inputs[0])
    num = N - 1
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num % 2 == 0:
        # half_l = math.floor(num / 2)
        # half = (half_l + half_l + 1) / 2
        half = num // 2
        append = num // 2
    else:
        half = (num + 1) // 2
        append = 0
        # half = math.floor(num / 2)
    return half * num + append


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
