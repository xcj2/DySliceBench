import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
inf = 10**9


def partition(a, p, r):
    # xがピボット
    x = a[r][1]
    i = p - 1
    for j in range(p, r):
        if a[j][1] <= x:
            i = i + 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i + 1


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)


def main():
    n = int(input())
    cards = []
    for i in range(n):
        c = input().split()
        cards.append((c[0], int(c[1])))

    stable_sorted_cards = sorted(cards, key=lambda x: x[1])
    quicksort(cards, 0, n-1)

    if cards != stable_sorted_cards:
        print('Not stable')
    else:
        print('Stable')

    for card in cards:
        print(card[0], card[1])


if __name__ == '__main__':
    main()

