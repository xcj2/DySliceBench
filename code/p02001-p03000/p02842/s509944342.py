import sys
import math

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    in_tax = int(inputs[0])
    not_tax = in_tax / 1.08
    kirisute = math.floor(not_tax)

    ks = [kirisute - 2, kirisute - 1, kirisute, kirisute + 1, kirisute + 2]
    for k in ks:
        c = math.floor(k * 1.08)
        if c == in_tax:
            return k
    return ':('


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
