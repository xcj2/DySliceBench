import copy

class Card:
    def __init__(self):
        self.suit = ''
        self.value = 0

def bubbleSort(C, N):
    for i in reversed(range(N)):
        for j in range(i):
            if C[j].value > C[j+1].value:
                C[j], C[j+1] = C[j+1], C[j]

def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        C[i], C[minj] = C[minj], C[i]

def isSame(C1, C2, N):
    for i in range(N):
        if C1[i].suit != C2[i].suit:
            return False
    return True

def main():
    N = int(input())
    list = input().split(" ")
    
    cards1 = []
    for i in range(N):
        card = Card()
        card.suit = list[i][0]
        card.value = int(list[i][1:])
        cards1.append(card)
    cards2 = copy.deepcopy(cards1)

    bubbleSort(cards1, N)
    selectionSort(cards2, N)

    for c in cards1:
        if c == cards1[len(cards1)-1]:
            print(c.suit + str(c.value))
            print("Stable")
        else:
            print(c.suit + str(c.value), end=" ")

    for c in cards2:
        if c == cards2[len(cards2)-1]:
            print(c.suit + str(c.value))
            if isSame(cards1,cards2,N):
                print("Stable")
            else:
                print("Not stable")
        else:
            print(c.suit + str(c.value), end=" ")

if __name__ == "__main__":
    main()
