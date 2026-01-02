from itertools import combinations as combi

class Dice():
    def __init__(self, up, back, right, left, front, down):
        self.up = up
        self.down = down
        self.right = right
        self.left = left
        self.front = front
        self.back = back
    
    def north(self):
        temp = self.up
        self.up = self.back
        self.back = self.down
        self.down = self.front
        self.front = temp
    
    def south(self):
        temp = self.up
        self.up = self.front
        self.front = self.down
        self.down = self.back
        self.back = temp
        
    def east(self):
        temp = self.up
        self.up = self.left
        self.left = self.down
        self.down = self.right
        self.right = temp
    
    def west(self):
        temp = self.up
        self.up = self.right
        self.right = self.down
        self.down = self.left
        self.left = temp
    
    def counterclockwise(self):
        temp = self.back
        self.back = self.left
        self.left = self.front
        self.front = self.right
        self.right = temp
    
    def clockwise(self):
        temp = self.back
        self.back = self.right
        self.right = self.front
        self.front = self.left
        self.left = temp
        
    def operate(self, op):
        if op == "N":
            self.north()
        elif op == "S":
            self.south()
        elif op == "E":
            self.east()
        elif op == "W":
            self.west()
        
    def fix_up(self, up):
        if self.down == up:
            self.north()
            self.north()
        elif self.right == up:
            self.west()
        elif self.left == up:
            self.east()
        elif self.front == up:
            self.south()
        elif self.back == up:
            self.north()

    def fix_back_with_fixed_up(self, back):
        if self.right == back:
            self.clockwise()
        elif self.left == back:
            self.counterclockwise()
        elif self.front == back:
            self.clockwise()
            self.clockwise()
            
    def equals_narrow_sense(self, dice):
        if self.up == dice.up and self.down == dice.down and self.right == dice.right and self.left == dice.left and self.back == dice.back and self.front == dice.front:
            return True
        else:
            return False

def is_equal_dice(dice1, dice2):
    for i in range(6):
        if 0 < i <= 3:
            dice1.north()
        elif i == 4:
            dice1.west()
        elif i == 5:
            dice1.east()
            dice1.east()

        for l in range(4):
            dice1.clockwise()

            for j in range(6):
                if 0 < j <= 3:
                    dice2.north()
                elif j == 4:
                    dice2.west()
                elif j == 5:
                    dice2.east()
                    dice2.east()

                for k in range(4):
                    dice2.clockwise()

                    if dice1.equals_narrow_sense(dice2):
                        return True
    return False

dice_n = int(input())

dice_lst = []
for _ in range(dice_n):
    up, back, right, left, front, down = map(int, input().split())
    dice_lst.append(Dice(up, back, right, left, front, down))
    
equal_flag = False
for pair in combi(dice_lst, 2):
    if is_equal_dice(pair[0], pair[1]):
        equal_flag = True
        break

if equal_flag:
    print("No")
else:
    print("Yes")
