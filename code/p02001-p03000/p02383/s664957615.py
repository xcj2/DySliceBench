class Dice:
    
    def __init__(self, val):
        self.top = val[0]
        self.flat1 = val[3]
        self.flat2 = val[1]
        self.flat3 = val[2]
        self.flat4 = val[4]
        self.bottom = val[5]
        
    def doSouth(self):
        temp = self.bottom
        self.bottom = self.flat2
        self.flat2 = self.top
        self.top = self.flat4
        self.flat4 = temp

    def doNorth(self):
        temp = self.bottom
        self.bottom = self.flat4
        self.flat4 = self.top
        self.top = self.flat2
        self.flat2 = temp

    def doWest(self):
        temp = self.top
        self.top = self.flat3
        self.flat3 = self.bottom
        self.bottom = self.flat1
        self.flat1 = temp


    def doEast(self):
        temp = self.top
        self.top = self.flat1
        self.flat1 = self.bottom
        self.bottom = self.flat3
        self.flat3 = temp
    
    def doget(self):
        list = [self.top, self.flat2, self.flat3, self.flat1, self.flat4, self.bottom]
        return(list)

def transform(dice, motion):
    if motion == 'S':
        dice.doSouth()
    elif motion == 'N':
        dice.doNorth()
    elif motion == 'W':
        dice.doWest()
    elif motion == 'E':
        dice.doEast()

N = input().split()
dice = Dice(N)
motion = input()
for i in range(len(motion)):
    transform(dice, motion[i])
print(dice.top)
