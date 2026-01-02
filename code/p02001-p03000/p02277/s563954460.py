# -*- coding:utf-8 -*-
import sys


class Card(object):
    def __init__(self, card):
        self._suit = card[0]
        self._value = int(card[1])

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__ == other.__dict__

    def __lt__(self, other):
        if other is None:
            return False
        return self._value < other._value

    def __le__(self, other):
        if other is None:
            return False
        return self._value <= other._value

    def __gt__(self, other):
        if other is None:
            return False
        return self._value > other._value

    def __ge__(self, other):
        if other is None:
            return False
        return self._value >= other._value

    def getValue(self):
        return self._value

    def __str__(self):
        return self._suit + " " + str(self._value)


def merge(lst, left, mid, right):
    L = lst[left: mid]
    R = lst[mid: right]
    l_len = len(L)
    r_len = len(R)
    i = 0
    j = 0
    for k in range(left, right):
        if l_len <= i:
            lst[k] = R[j]
            j += 1
        elif r_len <= j:
            lst[k] = L[i]
            i += 1
        elif L[i] <= R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1


def mergeSort(lst, left, right):
    if left + 1 < right:
        mid = (left + right) >> 1
        mergeSort(lst, left, mid)
        mergeSort(lst, mid, right)
        merge(lst, left, mid, right)


def partition(lst, p, r):
    x = lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
    i += 1
    tmp = lst[i]
    lst[i] = lst[r]
    lst[r] = tmp
    return i


def quicksort(lst, p, r):
    if p < r:
        q = partition(lst, p, r)
        quicksort(lst, p, q-1)
        quicksort(lst, q + 1, r)


if __name__ == "__main__":
    n = int(input())
    data = [val.split() for val in sys.stdin.readlines()]
    cards = [Card(card) for card in data]
    conf = cards[:]
    quicksort(cards, 0, n - 1)
    mergeSort(conf, 0, n)
    if cards == conf:
        print("Stable")
    else:
        print("Not stable")
    print("\n".join([str(card) for card in cards]))