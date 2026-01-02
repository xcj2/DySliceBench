import sys
from collections import deque

sys.setrecursionlimit(4100000)


def inputs(num_of_input):
    ins = [input() for i in range(num_of_input)]
    return ins


def solve(inputs):
    points = list(map(string_to_int, inputs))
    points = [p for p in points if p[2] != 0]
    if len(points) == 1:
        return "{} {} {}".format(points[0][0], points[0][1], points[0][2])
    for top_x in range(101):
        for top_y in range(101):
            is_correct = True
            p = points[0]
            prev_h = max(p[2] + abs(p[0] - top_x) + abs(p[1] - top_y), 0)
            for [px, py, ph] in points:
                top_h = max(ph + abs(px - top_x) + abs(py - top_y), 0)
                if top_h != prev_h:
                    is_correct = False
                    break
            if is_correct:
                return "{} {} {}".format(top_x, top_y, prev_h)


def string_to_int(string):
    return list(map(int, string.split()))


if __name__ == "__main__":
    N = int(input())
    ret = solve(inputs(N))
    print(ret)
