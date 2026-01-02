#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Aizu Online Judge. Quick Sort
import sys

class Card():
    def __init__(self, suit, val, pos):
        self.suit = suit
        self.val = val
        self.pos = pos

def partition(A, p, r):
    x = A[r].val
    i = p-1
    for n in range (p,r):
        if A[n].val <= x:
            i += 1
            A[i], A[n] = A[n], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

def check_stable(A):
    prev_val = None
    for card in A:
        if card.val == prev_val:
            if card.pos < prev_pos:
                print('Not stable')
                return
        prev_val = card.val
        prev_pos = card.pos

    print('Stable')
    return


n = int(sys.stdin.readline())
A = list()
for pos in range(n):
    suit, val_s = sys.stdin.readline().split()
    A.append(Card(suit, int(val_s), pos))

quicksort(A, 0, n-1)
check_stable(A)
for card in A:
    print(card.suit, card.val)

