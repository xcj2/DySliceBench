import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(N, K, inputs):
    trees = list(map(lambda x: int(x), inputs))
    trees.sort()

    min_diff = -1
    for i in range(K-1, N):
        diff = trees[i] - trees[i - K + 1]
        if min_diff == -1 or diff < min_diff:
            min_diff = diff
    return min_diff


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N, K] = string_to_int(input())
    ret = solve(N, K, inputs(N))
    print(ret)
