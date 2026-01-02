class Deck:
    def __init__(self, cards):
        """cards is a string of alphabetical letters
        """
        self.cards = cards

    def shuffle(self, h):
        """take h cards from the top of deck and move to bottom

        >>> deck = Deck("abcdeefab")
        >>> deck.shuffle(4)
        >>> str(deck)
        'eefababcd'
        >>> deck.shuffle(3)
        >>> str(deck)
        'ababcdeef'
        """
        self.cards = self.cards[h:] + self.cards[:h]

    def __str__(self):
        return self.cards


def run():
    while True:
        cards = input()
        if cards == '-':
            break

        deck = Deck(cards)
        times = int(input())

        for i in range(times):
            h = int(input())
            deck.shuffle(h)

        print(deck)


if __name__ == '__main__':
    run()
