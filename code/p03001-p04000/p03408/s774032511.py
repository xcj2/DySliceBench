import sys

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(blues, reds):
    blue_counts = {}
    red_counts = {}

    for b in blues:
        if b not in blue_counts:
            blue_counts[b] = 1
        else:
            blue_counts[b] += 1

    for r in reds:
        if r not in red_counts:
            red_counts[r] = 1
        else:
            red_counts[r] += 1

    max_count = 0
    for name, c in blue_counts.items():
        if name in red_counts:
            max_count = max(max_count, c - red_counts[name])
        else:
            max_count = max(max_count, c)
    return max_count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    [N] = string_to_int(input())
    blues = inputs(N)
    [M] = string_to_int(input())
    reds = inputs(M)
    ret = solve(blues, reds)
    print(ret)
