import math
def main():
    dice = Dice([int(a) for a in input().split()])
    commands = input()
    for d in range(len(commands)):
        dice.move(commands[d])
    dice.show()

class Dice():
    def __init__(self, surface):
        self.l = surface
 
    def move(self, dir):
        if(dir == 'N'):
            self.l = [self.l[1], self.l[5], self.l[2], self.l[3], self.l[0], self.l[4]]
        elif(dir == 'W'):
            self.l = [self.l[2], self.l[1], self.l[5], self.l[0], self.l[4], self.l[3]]
        elif(dir == 'E'):
            self.l = [self.l[3], self.l[1], self.l[0], self.l[5], self.l[4], self.l[2]]
        elif(dir == 'S'):
            self.l = [self.l[4], self.l[0], self.l[2], self.l[3], self.l[5], self.l[1]]

    def show(self):
        print(self.l[0])


main()
