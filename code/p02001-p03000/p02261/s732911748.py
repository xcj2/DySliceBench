import copy

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def bubblesort(n,a):
    flag = 1
    while flag:
        flag = False
        for i in reversed(range(1,n)):
            if a[i-1].value > a[i].value:
                a[i], a[i-1] = a[i-1], a[i]
                flag = True
    return a

def selectionsort(n,a):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j].value < a[minj].value:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    return a

def is_stable(before, after):
    n = 9
    lb = [[] for _ in range(n)]
    la = [[] for _ in range(n)]
    for i in range(len(before)):
        lb[before[i].value-1].append(before[i].suit)
        la[after[i].value-1].append(after[i].suit)
    if la == lb:
        print('Stable')
    else:
        print('Not stable')


if __name__ == '__main__':
    n = int(input())
    cards = [Card(x[0], int(x[1])) for x in input().split()]

    bubble_cards = bubblesort(n, copy.deepcopy(cards))
    selection_cards = selectionsort(n, copy.deepcopy(cards))

    print(' '.join(map(lambda x: x.suit+str(x.value), bubble_cards)))
    is_stable(cards, bubble_cards)

    print(' '.join(map(lambda x: x.suit+str(x.value), selection_cards)))
    is_stable(cards, selection_cards)








