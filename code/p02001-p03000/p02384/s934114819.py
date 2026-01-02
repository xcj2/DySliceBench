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

def MakeData(dice):
    num_data = 4 * len(my_label)-1
    
    dataset = list()
    data = [dice.top, dice.front, dice.right]

    dataset.append(data)
    
    isOnly = True
    
    while 0 < num_data:
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
my_label = [int(x) for x in input().split(" ")]
dice = Dice(my_label)
data = MakeData(dice)


q = int(input())
while q > 0:
    n_top,n_front = [int(x) for x in input().split(" ")]
    
    CheckData(data,n_top,n_front)
    
    q -= 1

