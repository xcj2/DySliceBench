import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    H = string_to_int(inputs[0])

    prev_h = -1
    max_count = 0
    count = 0
    for h in H:
        if prev_h == -1:
            prev_h = h
            continue

        if prev_h < h:
            max_count = max(max_count, count)
            count = 0
        else:
            count += 1

        prev_h = h
    max_count = max(max_count, count)
    return max_count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
