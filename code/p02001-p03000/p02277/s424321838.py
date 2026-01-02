class Card:
    def __init__(self, mark, numebr):
        super().__init__()
        self.mark = mark
        self.number = number

    def __lt__(self, other):
        return int(self.number) < int(other.number)


def partition(A, p, r):
    x = A[r].number
    i = p-1
    for j in range(p, r):
        if int(A[j].number) <= int(x):
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


if __name__ == "__main__":
    n = int(input())
    Cards = []
    Cards2 = []
    for _ in range(n):
        mark, number = input().split()
        Cards.append(Card(mark, int(number)))
        Cards2.append(Card(mark, int(number)))

    quickSort(Cards, 0, n-1)
    Cards2 = sorted(Cards2)

    stable = True
    for i in range(n):
        if not (Cards[i].mark == Cards2[i].mark and Cards[i].number == Cards2[i].number):
            stable = False

    if stable:
        print('Stable')
    else:
        print('Not stable')

    for card in Cards:
        print('{} {}'.format(card.mark, card.number))

