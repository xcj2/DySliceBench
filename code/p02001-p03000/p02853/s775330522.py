import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [A, B] = string_to_int(inputs[0])
    s = 0
    if A == 1:
        s += 300000
    elif A == 2:
        s += 200000
    elif A == 3:
        s += 100000

    if B == 1:
        s += 300000
    elif B == 2:
        s += 200000
    elif B == 3:
        s += 100000

    if A == 1 and B == 1:
        s += 400000
    return s


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
