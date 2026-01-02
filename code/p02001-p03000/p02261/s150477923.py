class Card:
    def __init__(self, card):
        self.value = int(card[1])
        self.card = card


def selectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
        if minj != i:
            tmp = A[i]
            A[i] = A[minj]
            A[minj] = tmp

    return A


def bubbleSort(A, N):
    flag = 1
    while flag:
        flag = 0
        for j in range(N-1, 0, -1):
            if A[j].value < A[j-1].value:
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1

    return A


def check_stable(A, cards):
    for num in range(1, 10):
        As = []
        Cs = []
        for a in A:
            if a.value == num:
                As.append(a.card)
        for c in cards:
            if c.value == num:
                Cs.append(c.card)

        if As != Cs:
            print("Not stable")
            return
    else:
        print("Stable")
        return


def main():
    N = int(input())
    cards = [Card(i) for i in input().split()]
    bubble_cards = bubbleSort(cards.copy(), N)
    selection_cards = selectionSort(cards.copy(), N)

    print(*[bc.card for bc in bubble_cards])
    check_stable(bubble_cards, cards)
    print(*[sc.card for sc in selection_cards])
    check_stable(selection_cards, cards)


if __name__ == "__main__":
    main()
