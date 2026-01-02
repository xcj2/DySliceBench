class Dice:
    def __init__(self,my_label):
        self.top,self.front,self.right,self.left,self.back,self.bottom = [int(x) for x in my_label]

    def Roll(self,i):
        if i == 0:
            self.top, self.front, self.right, self.left, self.back, self.bottom = \
            self.right, self.front, self.bottom, self.top, self.back, self.left
        
        if i == 1:
            self.top, self.front, self.right, self.left, self.back, self.bottom = \
            self.left, self.front, self.top, self.bottom, self.back, self.right
        
        if i == 2:
            self.top, self.front, self.right, self.left, self.back, self.bottom = \
            self.back, self.top, self.right, self.left, self.bottom, self.front
            
        if i == 3:
            self.top, self.front, self.right, self.left, self.back, self.bottom = \
            self.front, self.bottom, self.right, self.left, self.top, self.back

    def Open(self):
        print(self.top)

def CheckData(data,top,front):
    for i in range(len(data)):
        if(data[i][0] == top and data[i][1] == front):
            print(data[i][2])
            break
            
def CheckDice(n,data):
    #同じ物が見つかったら偽にしてbreak
    
    isEqual = False
    
    for i in range(n):
        for j in range(i+1,n):
            if(data[i] == data[j]):
                isEqual = True
                break
    
    if(isEqual == True):
        print("No")
    else:
        print("Yes")
                
def MakeData(dice):
    num_data = 4 * 6 -1
    
    dataset = list()
    data = [dice.top, dice.front, dice.right]

    dataset.append(data)
    
    isOnly = True
    
    n = 0
    while 0 < num_data:
        n += 1
        if (n > 1000):
            break
            
        data = [dice.top, dice.front, dice.right]

        isOnly = True
        for i in range (len(dataset)):
            if(data == dataset[i]):
                isOnly = False
                break
        if isOnly == True:
            dataset.append(data)
            dataset.sort()
            num_data -= 1
        
        dice.Roll(int(random.random() * 4))
        
    
        
    return dataset

import random

n = int(input())

my_label = [0] * n
dice = [0] * n
data = [0] * n

for i in range(n):
    my_label = [int(x) for x in input().split(" ")]
    
    dice = Dice(my_label)
    data[i] = MakeData(dice)

CheckDice(n,data)
