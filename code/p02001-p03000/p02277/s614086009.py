# coding: utf-8

class Card:
    def __init__(self, card, initial):
        self.mark = card[0]
        self.number = int(card[1])
        self.initial = initial

def partition(A, p, r):
    x = A[r].number
    i = p-1
    for j in range(p,r):
        if A[j].number <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
        
def isStable(A, n):
    flag = True
    for i in range(n-1):
        if A[i+1].number == A[i].number and A[i+1].initial < A[i].initial:
            flag = False
    return flag

def printCards(A, n):
    for i in range(n):
        print(A[i].mark, end=" ")
        print(A[i].number)

n = int(input().rstrip())
cards = []
for i in range(n):
    cards.append(Card(input().rstrip().split(), i))
quickSort(cards, 0, n-1)
if isStable(cards, n):
    print("Stable")
else:
    print("Not stable")

printCards(cards, n)
