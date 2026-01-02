# coding: utf-8


class Player:

    def __init__(self):
        self.point = 0

    def add_point(self, point):
        self.point += point

    def get_point(self):
        return self.point


def main():

    _ = int(input())
    cards = list(map(int, input().split(' ')))
    cards = sorted(cards, reverse=True)

    alice = Player()
    bob = Player()
    players = [alice, bob]
    for i, card in enumerate(cards):
        players[i % len(players)].add_point(card)

    print(alice.get_point() - bob.get_point())

    return 0


if __name__ == '__main__':
    main()
