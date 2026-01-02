def main() :
    n = int(input())
    cards = [Card(*input().split()) for i in range(n)]
    stableCards = sorted(cards[:], key=lambda c: c.number)
    quickSort(cards, 0, n - 1)
    print(isStable(cards, stableCards, n))
    list(map(lambda i : i.print_card(), cards))

def quickSort(cards, p, r) :
    if p < r:
        q = partion(cards, p, r)
        quickSort(cards, p, q - 1)
        quickSort(cards, q + 1, r)

def partion(cards, p, r) :
    x = cards[r]
    i = p
    for j in range(p, r + 1) :
        if int(cards[j].number) <= int(x.number) :
            cards[i], cards[j] = cards[j], cards[i]
            i += 1
    return i - 1

def isStable(a, b, n):
    for i in range(n):
        if a[i].prefix != b[i].prefix:
            return 'Not stable'

    return 'Stable'

class Card():
    def __init__(self, prefix, number):
        self.prefix = prefix
        self.number = number

    def print_card(self):
        print(self.prefix, self.number)

if __name__ == '__main__':
    main()

