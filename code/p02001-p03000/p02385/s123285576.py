import random
class Dice:
    def __init__(self, usr_input):
        self.eyes = list(map(int, usr_input.split()))
        self.pos = {label:eye for label, eye in zip(range(1, 7), self.eyes)}
        #self.com = list(command)

    def roll(self,c):
        self.eyes = [n for n in self.pos.values()]
        if c == 'E':
            self.pos[1] = self.eyes[3]
            self.pos[3] = self.eyes[0]
            self.pos[4] = self.eyes[5]
            self.pos[6] = self.eyes[2]
        elif c == 'N':
            self.pos[1] = self.eyes[1]
            self.pos[2] = self.eyes[5]
            self.pos[5] = self.eyes[0]
            self.pos[6] = self.eyes[4]
        elif c == 'S':
            self.pos[1] = self.eyes[4]
            self.pos[2] = self.eyes[0]
            self.pos[5] = self.eyes[5]
            self.pos[6] = self.eyes[1]
        elif c == 'W':
            self.pos[1] = self.eyes[2]
            self.pos[3] = self.eyes[5]
            self.pos[4] = self.eyes[0]
            self.pos[6] = self.eyes[3]

if __name__ == '__main__':
    dice1 = Dice(input())
    dice2 = Dice(input())
    def is_same(obj_1, obj_2):
        for i in range(720):
            if obj_1.pos == obj_2.pos:
                return True
            c = random.choice(['N','E','W','S'])
            obj_1.roll(c)
        return False
    if is_same(dice1, dice2):
        print('Yes')
    else:
        print('No')