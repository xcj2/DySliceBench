import sys
import itertools

class Dice:
    def __init__(self):
        self.front = '1'
        self.back = '6'
        self.top = '5'
        self.bottom = '2'
        self. right = '3'
        self.left = '4'
    def turnRight(self):
        temp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp
        return self.top
    def turnLeft(self):
        temp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp
        return self.top
    def turnFront(self):
        temp = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = temp
        return self.top
    def turnBack(self):
        temp = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = temp
        return self.top
    def __eq__(self, other):
        return (self.top, self.bottom, self.front, self.back, self.right, self.left) == other
    def __ne__(self, other):
        return (self.top, self.bottom, self.front, self.back, self.right, self.left) != other

def compdice(A, B):
    for rot1 in range(4):
        for rot2 in range(4):
            if A == B:
                return True
            B.turnRight()
        B.turnFront()
    B.turnRight()
    B.turnFront()
    for rot in range(4):
        if A == B:
            return True
        B.turnRight()
    B.turnBack()
    B.turnBack()
    for rot in range(4):
        if A == B:
            return True
        B.turnRight()
    return False

ans = 'Yes'
n = int(input())
dices = []
for line in range(n):
    dice = Dice()
    dice.top, dice.front, dice.right, dice.left, dice.back, dice.bottom = input().split()
    dices.append(dice)
dicepairs = itertools.combinations(dices, 2)
for dicepair in dicepairs:
    A, B = dicepair
    if compdice(A, B):
        ans = 'No'
print(ans)