# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0513

"""
import sys
from sys import stdin
from itertools import chain
input = stdin.readline


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


def cut(k):
    global cards
    yellow = cards[:k]
    blue = cards[k:]
    cards = blue + yellow


def shuffle():
    global cards
    yellow = cards[:N]
    blue = cards[N:]
    temp = [[y, b] for y, b in zip(yellow, blue)]
    cards = list(flatten(temp))


cards = []
N = 0
def main(args):
    global N
    global cards
    n = int(input())
    N = n
    m = int(input())

    cards = [x for x in range(1, (2*n)+1)]
    for _ in range(m):
        op = int(input())
        if op == 0:
            shuffle()
        else:
            cut(op)

    print('\n'.join(map(str, cards)))


if __name__ == '__main__':
    main(sys.argv[1:])
    