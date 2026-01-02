import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    X = int(inputs[0])
    NUM = 1000000
    items = [100, 101, 102, 103, 104, 105]
    r = X

    not_fin = True

    while r >= 100:
        amari = r % 100
        if r == 0:
            return 1
        if amari == 0:
            return 1

        matubi = amari % 10
        if amari >= 5:
            r -= 105
        else:
            r -= items[matubi]
    if r == 0:
        return 1
    return 0


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(1))
    print(ret)
