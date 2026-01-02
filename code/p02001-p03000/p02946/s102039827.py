import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [K, X] = string_to_int(inputs[0])
    ret = []
    for i in range(X - K + 1, X + K):
        if i >= -1000000 and i <= 1000000:
            ret.append(i)
    return ret


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    s = ""
    for i in ret:
        s += "{} ".format(i)
    print(s.strip())
