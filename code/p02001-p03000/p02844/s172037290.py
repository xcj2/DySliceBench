import sys
from itertools import combinations
from collections import Counter


sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    S = inputs[0]
    N = len(S)
    trees = {}

    trees[S[0]] = {S[1]: set(S[2])}

    prev = S[2]
    prevprev = S[1]
    for i, c in enumerate(S):
        if i <= 2:
            continue

        for first in trees.keys():
            for second in trees[first].keys():
                trees[first][second].add(c)
            if prev not in trees[first]:
                trees[first][prev] = set(c)
        if prevprev not in trees:
            trees[prevprev] = {prev: set(c)}
        prevprev = prev
        prev = c

    count = 0
    for first in trees:
        for second in trees[first]:
            count += len(trees[first][second])
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
