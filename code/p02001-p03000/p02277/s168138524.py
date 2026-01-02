from operator import attrgetter
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j].number <= x.number:
            i = i + 1
            tp = A[j]
            A[j] = A[i]
            A[i] = tp
        else:
            continue
    A[r] = A[i+1]
    A[i+1] = x
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


def main():
    n = int(input())
    A = []
    for _ in range(n):
        suit, num = map(str, input().split())
        A.append(Card(suit, int(num))) 
    comp = sorted(A, key=attrgetter('number'))
    quickSort(A, 0, n-1)
    if A == comp:
        print('Stable')
    else:
        print('Not stable')
    for p in A:
        print(p.suit, p.number)
main()
