import sys
import bisect

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def bis_insert(L, target, top=None, bottom=None):
    if top is None:
        top = len(L)
    if bottom is None:
        bottom = 0

    while bottom < top:
        half = (top + bottom) // 2
        if target > L[half]:
            bottom = half + 1
        else:
            top = half
    return bottom


def solve(inputs):
    L = string_to_int(inputs[0])
    L.sort()
    total_count = 0
    for i in range(len(L) - 2):
        for j in range(i + 1, len(L)-1):
            a = L[i]
            b = L[j]
            target = a + b
            # r = bis_insert(L, target)
            r = bisect.bisect_left(L, target)
            total_count += r - j - 1
    return total_count


def string_to_int(string):
    return list(map(lambda x: int(x), string.split()))


if __name__ == "__main__":
    input()
    ret = solve(inputs(1))
    print(ret)
