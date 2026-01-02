class Dice:
    def __init__(self, dice: list):
        self.top = dice[0]
        self.bottom = dice[5]
        self.front = dice[1]
        self.behind = dice[4]
        self.right = dice[2]
        self.left = dice[3]

    def __eq__(self, other):
        if not isinstance(other, Dice):
            return NotImplemented
        return self.top == other.top and self.bottom == other.bottom and self.front == other.front \
                and self.behind == other.behind and self.right == other.right

    def roll(self, direction: str):
        buffer = self.top
        if direction == 'E':
            self.top = self.left
            self.left = self.bottom
            self.bottom = self.right
            self.right = buffer
        elif direction == 'N':
            self.top = self.front
            self.front = self.bottom
            self.bottom = self.behind
            self.behind = buffer
        elif direction == 'S':
            self.top = self.behind
            self.behind = self.bottom
            self.bottom = self.front
            self.front = buffer
        else:
            self.top = self.right
            self.right = self.bottom
            self.bottom = self.left
            self.left = buffer

    def turn(self):
        buffer = self.front
        self.front = self.right
        self.right = self.behind
        self.behind = self.left
        self.left = buffer


def main():
    dice1, dice2 = [Dice(list(map(int, input().split()))) for _ in range(2)]
    for _ in range(2):
        for _ in range(4):
            for _ in range(4):
                if dice1 == dice2:
                    print('Yes')
                    return
                dice2.turn()
            dice2.roll('N')
        dice2.roll('E')
    print('No')


if __name__ == '__main__':
    main()

