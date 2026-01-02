import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    p = string_to_int(inputs[0])

    diff_point = []
    for i, num in enumerate(range(1, len(p)+1)):
        if num != p[i]:
            diff_point.append(i)
    if len(diff_point) == 2 or len(diff_point) == 0:
        return "YES"
    return "NO"


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
