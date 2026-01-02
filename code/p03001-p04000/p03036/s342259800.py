import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [r, D, x] = string_to_int(inputs[0])

    ret = deque([x])
    for _ in range(0, 10):
        ret.append(r * ret[-1] - D)

    ret.popleft()
    ret_str = ""
    for i in ret:
        ret_str += "{:d}\n".format(i)
    ret_str.strip()

    return ret_str


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
