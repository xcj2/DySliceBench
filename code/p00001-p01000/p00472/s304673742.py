# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0549
AC
"""
import sys
from sys import stdin
from itertools import accumulate
input = stdin.readline
import array

def main(args):
    n, m = map(int, input().split())
    distances = [int(input()) for _ in range(n-1)]
    inns = list(accumulate(distances))
    moves = [int(input()) for _ in range(m)]

    inns.insert(0, 0)
    pos = 0
    total_distance = 0
    for m in moves:
        new_pos = pos + m
        total_distance += abs(inns[new_pos] - inns[pos])
        pos = new_pos

    print(total_distance % 100000)



def main2(args):
    n, m = map(int, input().split())

    pos = 0
    inns = array.array('Q', [0])
    for _ in range(n-1):
        pos += int(input())
        inns.append(pos)
    moves = [int(input()) for _ in range(m)]

    pos = 0
    total_distance = 0
    for m in moves:
        new_pos = pos + m
        total_distance += abs(inns[new_pos] - inns[pos])
        pos = new_pos

    print(total_distance % 100000)



def main3(args):
    n, m = map(int, input().split())

    pos = 0
    inns = {0: 0}
    for i in range(n-1):
        pos += int(input())
        inns[i+1] = pos
    moves = [int(input()) for _ in range(m)]

    pos = 0
    total_distance = 0
    for m in moves:
        new_pos = pos + m
        total_distance += abs(inns[new_pos] - inns[pos])
        pos = new_pos

    print(total_distance % 100000)



if __name__ == '__main__':
    main3(sys.argv[1:])