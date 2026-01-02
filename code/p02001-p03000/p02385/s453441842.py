import sys
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
def judge(obj1, obj2):
    if obj1 == obj2:
        print('Yes')
        sys.exit()
    else:
        return

A = Dice()
B = Dice()
A.top, A.front, A.right, A.left, A.back, A.bottom = input().split()
B.top, B.front, B.right, B.left, B.back, B.bottom = input().split()

for rot1 in range(4):
    for rot2 in range(4):
        judge(A, B)
        B.turnRight()
    B.turnFront()
B.turnRight()
B.turnFront()
for rot in range(4):
    judge(A,B)
    B.turnRight()
B.turnBack()
B.turnBack()
for rot in range(4):
    judge(A,B)
    B.turnRight()
print('No')

    