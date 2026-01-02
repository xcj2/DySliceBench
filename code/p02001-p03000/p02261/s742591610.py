#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import copy


class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value


def isStable(C1, C2, N):
  for i in range(N):
    if (C1[i].suit != C2[i].suit):
      return False
  return True


def printCard(C):
  out = [(c.suit + c.value) for c in C]
  print(' '.join(out))


def validate_num_input(C, N):
  if len(C) != N:
    print("[ERROR] Number of Card caracter is invalid")
    sys.exit()


def bubbleSort(C, N):
  for i in range(N):
    for j in range(N - 1, i, -1):
      if C[j].value < C[j - 1].value:
        C[j], C[j - 1] = C[j - 1], C[j]
  return C


def selectionSort(C, N):
  for i in range(N):
    minj = i
    for j in range(i, N):
      if C[j].value < C[minj].value:
        minj = j
    C[i], C[minj] = C[minj], C[i]
  return C


def main():
  N = int(input())
  C = [x for x in input().split()]

  validate_num_input(C, N)

  C1 = [Card(c[0], c[1]) for c in C]
  C2 = copy.deepcopy(C1)

  C1 = bubbleSort(C1, N)
  printCard(C1)
  print("Stable")

  C2 = selectionSort(C2, N)
  printCard(C2)
  if (isStable(C1, C2, N)):
    print("Stable")
  else:
    print("Not stable")


if __name__ == '__main__':
  main()

