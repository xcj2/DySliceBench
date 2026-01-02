#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def isSquared(n):
    for i in range(128):
        if i ** 2 > n:
            return False
        elif i ** 2 == n:
            return True
    return False


def squaredDist(x, y):
    s = 0
    for i, j in zip(x, y):
        s += (i - j)**2
    return s


def solve():
    N, D = list(map(int, input().split()))
    points = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if isSquared(squaredDist(points[i], points[j])):
                count += 1
    return count


def main():
    print(solve())


if __name__ == "__main__":
    main()
