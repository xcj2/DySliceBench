#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Card(object):

    def __init__(self, card):
        self.card = card
        self.suit = card[0]
        self.value = int(card[1:])

    def __str__(self):
        return str(self.card)


def print_array(a):
    print(" ".join(map(str, a)))


def bubblesort(cards, n):
    c = cards[::]
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if c[j].value < c[j - 1].value:
                (c[j], c[j - 1]) = (c[j - 1], c[j])
    return c


def selectionsort(cards, n):
    c = cards[::]
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if c[j].value < c[minj].value:
                minj = j
        (c[i], c[minj]) = (c[minj], c[i])
    return c


def main():
    n = int(input())
    cards = list(map(Card, input().split()))
    b = bubblesort(cards, n)
    print_array(b)
    print("Stable")
    s = selectionsort(cards, n)
    print_array(s)
    if b == s:
        print("Stable")
    else:
        print("Not stable")


if __name__ == "__main__":
    main()