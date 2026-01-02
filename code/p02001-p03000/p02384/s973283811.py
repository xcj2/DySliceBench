import random

def main():
    dir = ['W', 'N', 'S', 'E']
    dice = Dice([int(a) for a in input().split()])
    n = int(input())
    for _ in range(n):
        top, front = (int(x) for x in input().split())
        while True:
            if top == dice.getSuf(0) and front == dice.getSuf(1):
                print(dice.getSuf(2))
                break
            dice.move(random.choice(dir))


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
    
    def getSuf(self, surface):
        return self.l[surface]


main()
