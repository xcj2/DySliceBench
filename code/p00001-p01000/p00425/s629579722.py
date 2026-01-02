class Dice:
    def __init__(self):
        self.total = 1
        self.up = 1
        self.s = 2
        self.e = 3

    def north(self):
        self.up, self.s = self.s, 7 - self.up
        self.total += self.up

    def south(self):
        self.up, self.s = 7 - self.s, self.up
        self.total += self.up

    def east(self):
        self.up, self.e = 7 - self.e, self.up
        self.total += self.up

    def west(self):
        self.up, self.e = self.e, 7 - self.up
        self.total += self.up

    def right(self):
        self.s, self.e = self.e, 7 - self.s
        self.total += self.up

    def left(self):
        self.s, self.e = 7 - self.e, self.s
        self.total += self.up

    def exe(self, cmd):
        if 'N' in cmd:
            self.north()
        elif 'S' in cmd:
            self.south()
        elif 'E' in cmd:
            self.east()
        elif 'W' in cmd:
            self.west()
        elif 'R' in cmd:
            self.right()
        elif 'L' in cmd:
            self.left()

def solve(N):
    dice = Dice()
    for i in range(N):
        cmd = input()
        dice.exe(cmd)

    print(dice.total)

while True:
    N = int(input())
    if N == 0:
        break
    solve(N)