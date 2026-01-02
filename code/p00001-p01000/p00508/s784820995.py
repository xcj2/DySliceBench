# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0585

"""
import sys
from sys import stdin
input = stdin.readline


def closest_part1(points, n):
    # ?????¬???p324???
    if n <= 1:
        return float('inf')
    m = n // 2
    x = points[m][0]
    d = min(closest_part1(points[:m], m), closest_part1(points[m:], n-m))

    points.sort(key=lambda x:x[1])
    b = []
    for i in range(n):
        if (points[i][0] - x)**2 >= d:
            continue
        for j in range(len(b)):
            dx = points[i][0] - b[-j-1][0]
            dy = points[i][1] - b[-j-1][1]
            if dy**2 >= d:
                break
            d = min(d, (dx**2 + dy**2))
        b.append(points[i])
    return d


def closest_part2(points, n):
    if n <= 1:
        return float('inf')
    m = n // 2
    x = points[m][0]
    d = min(closest_part2(points[:m], m), closest_part2(points[m:], n-m))
    points.sort(key=lambda p:p[1])
    b = []
    for p in points:
        if (p[0] - x)**2 >= d:
            continue
        for q in b:
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            if dy**2 >= d:
                break
            d = min(d, (dx**2 + dy**2))
        b.insert(0, p)
    return d


def closest_part3(points, n):
    if n <= 1:
        return float('inf')
    m = n // 2
    x = points[m][0]
    d = min(closest_part3(points[:m], m), closest_part3(points[m:], n-m))
    points.sort(key=lambda p:p[1])
    b = []
    for p in points:
        if (p[0] - x)**2 >= d:
            continue
        for q in b[::-1]:
            dx = p[0] - q[0]
            dy = p[1] - q[1]
            if dy**2 >= d:
                break
            d = min(d, (dx**2 + dy**2))
        b.append(p)
    return d


def main(args):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.sort()               #  x????????§??????????????????

    result = closest_part3(points, n)
    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
    