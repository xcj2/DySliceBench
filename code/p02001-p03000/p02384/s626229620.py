# -*- coding: utf-8 -*-
# ITP1_11_B

class Dice:
    def __init__(self, num):
        self.num = num
        
    def show_r(self):
        """ 出目を表示する """
        print(self.num[2])
        
    def roll(self, direction):
        """ 転がす処理 """
        data = []
        new_num = []
        if direction == "N":
            data = [1, 5, 2, 3, 0, 4]
        elif direction == "S":
            data = [4, 0, 2, 3, 5, 1]
        elif direction == "E":
            data = [3, 1, 0, 5, 4, 2]
        elif direction == "W":
            data = [2, 1, 5, 0, 4, 3]
        elif direction == "L":
            data = [0, 2, 4, 1, 3, 5]
        elif direction == "R":
            data = [0, 3, 1, 4, 2, 5]

        for i in data:
            new_num.append(self.num[i])
        self.num = new_num
        
def dice_roll1(dice, dice_tf):
    dice_roll = ""
    top = dice_tf[0]
    
    if dice.num.index(top) == 1:
        dice_roll = "N"
    elif dice.num.index(top) == 2:
        dice_roll = "W"
    elif dice.num.index(top) == 3:
        dice_roll = "E"
    elif dice.num.index(top) == 4:
        dice_roll = "S"
    elif dice.num.index(top) == 5:
        dice_roll = "NN"
        
    return dice_roll

def dice_roll2(dice, dice_tf):
    dice_roll = ""
    front = dice_tf[1]
    
    if dice.num.index(front) == 2:
        dice_roll = "L"
    elif dice.num.index(front) == 3:
        dice_roll = "R"
    elif dice.num.index(front) == 4:
        dice_roll = "LL"
        
    return dice_roll

dice1 = Dice(list(map(int, input().split())))

dice_tf = []
for i in range(int(input())):
    dice_tf.append(list(map(int, input().split())))

for i in dice_tf:
    direction = dice_roll1(dice1, i)
    for j in direction:
        dice1.roll(j)
    
    direction = dice_roll2(dice1, i)
    for j in direction:
        dice1.roll(j)
        
    dice1.show_r()
