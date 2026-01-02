import sys
import math
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, M, inputs):
    likes = [string_to_int(i) for i in inputs]
    everyone_likes = {n for n in range(1, M+1)}

    for l in likes:
        like_set = set()
        for i, f in enumerate(l):
            if i == 0:
                continue
            like_set.add(f)

        everyone_likes = everyone_likes & like_set
    return len(everyone_likes)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, M] = string_to_int(input())
    ret = solve(N, M, inputs(N))
    print(ret)