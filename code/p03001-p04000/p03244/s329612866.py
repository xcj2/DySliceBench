import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    V = string_to_int(inputs[0])
    N = len(V)
    N_HALF = N // 2
    counts = {
        0: {},
        1: {}
    }
    for i, v in enumerate(V):
        key = i % 2
        if v in counts[key]:
            counts[key][v] += 1
        else:
            counts[key][v] = 1

    counts_sorted = []
    for i in range(2):
        counts_sorted.append(
            sorted(list(counts[i].items()), key=lambda x: x[1], reverse=True)
        )

    def count_replace(first, first_i, second, second_i):
        replace_count = N_HALF - counts_sorted[first][first_i][1]
        replace_count += N_HALF - counts_sorted[second][second_i][1]
        return replace_count

    if counts_sorted[0][0] == counts_sorted[1][0]:
        len_0 = len(counts_sorted[0])
        len_1 = len(counts_sorted[1])
        if len_0 == 1 and len_1 == 1:
            return N_HALF
        elif len_0 == 1:
            return N_HALF - counts_sorted[1][1][1]
        elif len_1 == 1:
            return N_HALF - counts_sorted[0][1][1]
        else:
            cs = []
            cs.append(count_replace(0, 0, 1, 1))
            cs.append(count_replace(0, 1, 1, 0))
            return min(cs)

    else:
        return count_replace(0, 0, 1, 0)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
