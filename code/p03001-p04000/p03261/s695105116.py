import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    W = inputs
    appeared = set()
    prev = ''
    for w in W:
        if w in appeared:
            return "No"
        appeared.add(w)
        if not (prev == '' or w[0] == prev):
            return "No"
        prev = w[-1]
    return "Yes"


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)