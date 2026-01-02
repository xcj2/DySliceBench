import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [D] = string_to_int(inputs[0])
    if D == 22:
        return "Christmas Eve Eve Eve"
    if D == 23:
        return "Christmas Eve Eve"
    if D == 24:
        return "Christmas Eve"
    if D == 25:
        return "Christmas"
    return ""


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
