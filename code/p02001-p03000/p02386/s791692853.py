#coding:utf-8
#1_11_C

class Dice:
    def __init__(self, ary):
        self.top, self.south, self.east, self.west, self.north, self.bottom = ary

    def roll_n(self):
        self.top, self.north, self.bottom, self.south = self.south, self.top, self.north, self.bottom

    def roll_e(self):
        self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom

    def twist(self):
        self.north, self.east, self.south, self.west = self.west, self.north, self.east, self.south

    def isEqual(self, dice):
        if self.top == dice.top and self.south == dice.south and self.east == dice.east and self.west == dice.west and self.north == dice.north and self.bottom == dice.bottom:
            return True
        else:
            return False

def isSame(diceX,diceY):
    flag = False
    
    for i in range(6):
        if i % 2 == 0:
            diceX.roll_n()
        else:
            diceX.roll_e()
    
        for j in range(4):
            if diceX.isEqual(diceY):
                flag = True
                break
            else:
                diceX.twist()
    
        if flag:
            break
    
    if flag:
        return True
    else:
        return False

n = int(input())
dices = [Dice(map(int,input().split())) for i in range(n)]

flag = False
for i in range(len(dices)):
    for j in range(i+1, len(dices)):
        if isSame(dices[i],dices[j]):
            flag = True

if not flag:
    print('Yes')
else:
    print('No')