import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = string_to_int(inputs[0])
    s_sum = deque([0])
    for s in S:
        s_sum.append(s_sum[-1] + s)
    s_sum.popleft()

    min_diff = None
    for i in range(len(s_sum)):
        front = s_sum[i]
        back = s_sum[-1] - front
        d = abs(front - back)
        if min_diff is None or min_diff > d:
            min_diff = d
    return min_diff


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
