class Dice():
    def __init__(self, arr):
        self.top = arr[0]
        self.front = arr[1]
        self.right = arr[2]
        self.left = arr[3]
        self.back = arr[4]
        self.bottom = arr[5]
        
    def rotate(self, direction):
        if direction == "N":
            self.back, self.top, self.front, self.bottom = \
            self.top, self.front, self.bottom, self.back
        elif direction == "S":
            self.front, self.bottom, self.back, self.top = \
            self.top, self.front, self.bottom, self.back
        elif direction == "E":
            self.right, self.bottom, self.left, self.top = \
            self.top, self.right, self.bottom, self.left
        elif direction == "W":
            self.left, self.bottom, self.right, self.top = \
            self.top, self.left, self.bottom, self.right
        elif direction == "R": # clockwise
            self.front, self.right, self.back, self.left =\
            self.right, self.back, self.left, self.front
            
    def get_faces(self):
        return [self.top, self.front, self.right, self.left,
               self.back, self.bottom]
    
n = int(input())
dice_list = []
for _ in range(n):
    dice_list.append(Dice(input().split()))
    
def is_same(dice1, dice2):
    flag = False
    
    if len(dice1.get_faces() and dice2.get_faces()) == 6:
        direction_list = ["", "S", "E", "S", "E", "S"]
        for direction in direction_list:
            dice2.rotate(direction)
            
            for i in range(4):
                if dice1.get_faces() == dice2.get_faces():
                    flag = True
                    break                  
                dice2.rotate("R")
                
            if flag:
                break
                
    return flag

flag = True

for i in range(n-1):
    for j in range(i+1, n):
        if is_same(dice_list[i], dice_list[j]):
            flag = False
            
if flag:
    print("Yes")
else:
    print("No")
