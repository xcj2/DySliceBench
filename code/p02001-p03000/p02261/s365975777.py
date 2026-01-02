# -*- coding: utf-8 -*-
def bubble(a):
    card = a[:]
    size = len(card)
    for i in range(size):
        for j in range(size - 1, i, -1):
            if card[j][1] < card[j - 1][1]:
                card[j], card[j - 1] = card[j - 1], card[j]
    return card


def selection(a):
    card = a[:]
    size = len(card)
    for i in range(size):
        minj = i
        for j in range(i, size):
            if card[j][1] < card[minj][1]:
                minj = j
        if minj != i:
            card[i], card[minj] = card[minj], card[i]
    return card


def is_stable(a, b):
    size = len(a)
    for i in range(size):
        if a[i][0] != b[i][0]:
            return False
    return True


def main():
    n = int(input())
    cards = input().split()
    a = bubble(cards)
    b = selection(cards)

    print(*a)
    print("Stable")
    print(*b)
    print("Stable" if is_stable(a, b) else "Not stable")


if __name__ == '__main__':
    main()

