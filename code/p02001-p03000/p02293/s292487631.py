#!/usr/bin/env python3
# CGL_2_A: Segments/Lines - Parallel/Orthogonal


def is_parallel(v1, v2):
    return dot(orthogonal(v1), v2) == 0


def is_orthogonal(v1, v2):
    return dot(v1, v2) == 0


def dot(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return x1 * x2 + y1 * y2


def orthogonal(v):
    x, y = v
    return -y, x


def run():
    q = int(input())

    for _ in range(q):
        x0, y0, x1, y1, x2, y2, x3, y3 = [int(i) for i in input().split()]

        v1 = (x1-x0, y1-y0)
        v2 = (x3-x2, y3-y2)

        if is_parallel(v1, v2):
            print(2)
        elif is_orthogonal(v1, v2):
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    run()

