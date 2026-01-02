import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, K] = string_to_int(inputs[0])
    count_a = 0
    count_b = 0
    for i in range(1, N+1):
        if i % K == 0:
            count_a += 1
        if i % K == K/2:
            count_b += 1

    count = count_a ** 3
    if K % 2 == 0:
        count += count_b ** 3
    return count


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
