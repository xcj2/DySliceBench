# coding: utf-8
import copy
class Card:
    def __init__(self, card, initial):
        self.card = card
        self.mark = card[0]
        self.number = int(card[1])
        self.initial = initial

def bubbleSort(c, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if c[j].number < c[j-1].number:
                c[j], c[j-1] = c[j-1], c[j]

def selectionSort(c, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if c[j].number < c[minj].number:
                minj = j
        c[i], c[minj] = c[minj], c[i]

def printCards(cards, n):
    for i in range(n):
        print(cards[i].card,end="")
        if i == n -1:
            print()
        else:
            print(" ",end="")

def isStable(cards, n):
    for i in range(n-1):
        if cards[i].number == cards[i+1].number and cards[i].initial > cards[i+1].initial:
            return False
    return True

n = int(input().rstrip())
data = input().rstrip().split()
cards = []
for i in range(n):
    cards.append(Card(data[i], i))

init = copy.copy(cards)
bubbleSort(cards, n)
printCards(cards, n)
print("Stable" if isStable(cards, n) else "Not stable")
selectionSort(init, n)
printCards(init, n)
print("Stable" if isStable(init, n) else "Not stable")
