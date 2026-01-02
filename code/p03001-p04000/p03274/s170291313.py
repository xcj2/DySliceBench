import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, K, inputs):
    candles = string_to_int(inputs[0])
    min_distance = -1
    for i in range(0, N-K+1):
        left = candles[i]
        right = candles[i+K-1]
        distance = 0
        if left <= 0 and right <= 0:
            distance = abs(left) - abs(right) + abs(0 - right)
        elif left >= 0 and right >= 0:
            distance = right
        else:
            if abs(right) > abs(left):
                distance = abs(left) + abs(left) + abs(right)
            else:
                distance = abs(right) + abs(right) + abs(left)
        if min_distance == -1 or min_distance > distance:
            min_distance = distance

    return min_distance


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    [N, K] = string_to_int(input())
    ret = solve(N, K, inputs(1))
    print(ret)
