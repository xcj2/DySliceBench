class Dice:
    def __init__(self, dice: list):
        self.top = dice[0]
        self.bottom = dice[5]
        self.front = dice[1]
        self.behind = dice[4]
        self.right = dice[2]
        self.left = dice[3]

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
    dice = Dice(list(map(int, input().split())))
    for _ in range(int(input())):
        top, front = map(int, input().split())
        while True:
            if dice.right != top and dice.left != top:
                break
            dice.turn()
        while dice.top != top:
            dice.roll('N')
        while dice.front != front:
            dice.turn()
        print(dice.right)


if __name__ == '__main__':
    main()

