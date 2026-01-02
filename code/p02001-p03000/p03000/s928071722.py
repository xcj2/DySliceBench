import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    [N, X] = string_to_int(inputs[0])
    L = string_to_int(inputs[1])

    step = 0
    count = 1
    for i in range(1, N + 1):
        step += L[i - 1]

        if step <= X:
            count += 1
        else:
            break
    return count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    ret = solve(inputs(2))
    print(ret)
