def bubbleSort(cards, N):
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if cards.numbers[j] < cards.numbers[j - 1]:
                cards.swap(j, j-1)
                flag = True
    return cards

def selectionSort(cards,N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if cards.numbers[j] < cards.numbers[minj]:
                minj = j
        if minj != i:
            cards.swap(i, minj)
    return cards

class Cards(object):
    
    def __init__(self, cards):
        self.cards = cards
        self.numbers = [int(card[1]) for card in cards]

    def filter_by_number(self, number):
        return [card for card in self.cards if card.endswith(str(number))]

    def swap(self, i, j):
        self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        self.numbers = [int(card[1]) for card in self.cards]

    def show(self):
        print(' '.join(self.cards))

    def is_stable(self, cards):
        for n in range(1,10):
            suits_x = self.filter_by_number(str(n))
            suits_y = cards.filter_by_number(str(n))
            if suits_x != suits_y:
                return False
        return True

    def copy(self):
        return Cards([card for card in self.cards])

def run():
    n = int(input())
    cards = Cards(input().split())
    cards_sorted = bubbleSort(cards.copy(),n)
    cards_sorted.show()
    if cards.is_stable(cards_sorted):
        print('Stable')
    else:
        print('Not stable')

    cards_sorted = selectionSort(cards.copy(),n)
    cards_sorted.show()
    if cards.is_stable(cards_sorted):
        print('Stable')
    else:
        print('Not stable')

if __name__ == '__main__':
    run()
