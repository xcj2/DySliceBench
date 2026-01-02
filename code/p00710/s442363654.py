class Deck:

    def __init__(self, card_num):
        self.deck_list = self.make_deck(card_num)

    def make_deck(self, card_num):
        deck_list = [None] * card_num
        order = 0
        for i in reversed(range(1, card_num + 1)):
           deck_list[order] = i
           order += 1
        return deck_list

    def shuffled(self, cut_pos1, cut_pos2):
        above_card = self.deck_list[0:cut_pos1]
        below_card = self.deck_list[cut_pos1:cut_pos2]
        remain_card = self.deck_list[cut_pos2:]
        self.deck_list = below_card + above_card + remain_card


def get_two_int():
    two_int = input().split()
    for i in range(2):
        two_int[i] = int(two_int[i])
    return two_int


if __name__ == "__main__":
    while True:
        card_num, shuffle_num = get_two_int()
        if card_num == shuffle_num == 0:
            break
        deck = Deck(card_num)
        for i in range(shuffle_num):
            c, p = get_two_int()
            cut_pos1 = c - 1
            cut_pos2 = c - 1 + p
            deck.shuffled(cut_pos1, cut_pos2)
        print(deck.deck_list[0])

