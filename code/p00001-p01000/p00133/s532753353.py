# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0133

"""
import sys
from sys import stdin
input = stdin.readline


def rotate_ccw(data):
    A = [[''] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            A[i][j] = data[j][7-i]

    for l in A:
        print(''.join(l))
    return A


def rotate_cw(data):
    A = [[''] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            A[i][j] = data[7-j][i]

    for l in A:
        print(''.join(l))
    return A


def main(args):
    data = []
    for _ in range(8):
        data.append(list(input().strip()))

    print('90')
    data = rotate_cw(data)
    print('180')
    data = rotate_cw(data)
    print('270')
    data = rotate_cw(data)


if __name__ == '__main__':
    main(sys.argv[1:])
    