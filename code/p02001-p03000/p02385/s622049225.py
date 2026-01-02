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
            
def CheckDice(data1,data2):
    if(data1 == data2):
        print("Yes")
        
    else:
        print("No")

def MakeData(dice):
    num_data = 4 * 6 -1
    
    dataset = list()
    data = [dice.top, dice.front, dice.right]

    dataset.append(data)
    
    isOnly = True
    
    n = 0
    while 0 < num_data:
        n += 1
        if (n > 1000):break
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

my_label1 = [int(x) for x in input().split(" ")]
my_label2 = [int(x) for x in input().split(" ")]

dice1 = Dice(my_label1)
dice2 = Dice(my_label2)

data1 = MakeData(dice1)
data2 = MakeData(dice2)

CheckDice(data1,data2)
