import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [L, R] = string_to_int(inputs[0])

    if R - L >= 2019:
        return 0

    min = L * R
    for i in range(L, R):
        for j in range(i+1, R+1):
            c = (i*j) % 2019
            if min > c:
                min = c
    return min


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
