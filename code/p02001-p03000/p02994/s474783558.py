import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, L] = string_to_int(inputs[0])
    apples = [x + L for x in range(0, N)]
    min_i = 0
    for i in range(1, len(apples)):
        if abs(apples[min_i]) > abs(apples[i]):
            min_i = i
    apples.pop(min_i)

    return sum(apples)


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
