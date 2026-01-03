

class Player:

    def __init__(self, name, s):
        self.name = name
        self.cards = list(s)

    @property
    def is_winner(self):
        return len(self.cards) == 0

    def _drop(self):
        dropped = self.cards.pop(0)
        return dropped

    def play(self):
        if len(self.cards) >= 1:
            dropped = self._drop()
            return dropped
        return None

    def __str__(self):
        return self.name

A=Player("A", input())
B=Player("B", input())
C=Player("C", input())

def get_player(ch):
    if ch == 'a':
        return A
    elif ch == 'b':
        return B
    elif ch == 'c':
        return C
    else:
        raise ValueError('unknown char {}'.format(ch))


player = get_player(A.play())
if A.is_winner:
    print('A')
else:
    while player is not None:
        if player.is_winner:
            print(str(player))
            break
        next_ch = player.play()
        player = get_player(next_ch)

