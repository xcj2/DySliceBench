import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    N = int(inputs[0])
    if N == 1:
        return "Yes"
    if N > 81:
        return "No"
    for i in range(2, 10):
        if N % i == 0:
            for j in range(1, 10):
                if i * j == N:
                    return "Yes"
    return "No"


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
