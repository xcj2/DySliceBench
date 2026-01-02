class Dice:
    def __init__(self, label):
        self.label = label.copy()
    
    def rotateS(self):
        """[1, 2, 6, 5] -> [5, 1, 2, 6]"""
        t = self.label[1]
        self.label[1] = self.label[5]
        self.label[5] = self.label[6]
        self.label[6] = self.label[2]
        self.label[2] = t

    def rotateN(self):
        t = self.label[1]
        self.label[1] = self.label[2]
        self.label[2] = self.label[6]
        self.label[6] = self.label[5]
        self.label[5] = t
    
    def rotateW(self):
        t = self.label[1]
        self.label[1] = self.label[3]
        self.label[3] = self.label[6]
        self.label[6] = self.label[4]
        self.label[4] = t
    
    def rotateE(self):
        t = self.label[1]
        self.label[1] = self.label[4]
        self.label[4] = self.label[6]
        self.label[6] = self.label[3]
        self.label[3] = t

    def rotateR(self):
        'SWN = R'
        t = self.label[3]
        self.label[3] = self.label[2]
        self.label[2] = self.label[4]
        self.label[4] = self.label[5]
        self.label[5] = t

    def rotateL(self):
        'SEN = L'
        t = self.label[3]
        self.label[3] = self.label[5]
        self.label[5] = self.label[4]
        self.label[4] = self.label[2]
        self.label[2] = t


def compare(dice1, dice2):
    if (dice1.label == dice2.label):
        return True
    else:
        return False

def verify(dice1, dice2):
    dice_t = Dice(dice2.label)
    numS = 0
    for i in range(0,4):
        numR = 0
        for _ in range(0,4):
            debugprint(dice1, dice_t)
            if (compare(dice1, dice_t)):
                return True
            dice_t.rotateR()
            numR += 1
        #print(numR)
        dice_t.rotateS()
        numS += 1
    #print(numS)

    dice_t.rotateE()
    for _ in range(0,4):
        debugprint(dice1, dice_t)
        if (compare(dice1, dice_t)):
            return True
        dice_t.rotateR()

    dice_t.rotateE()
    dice_t.rotateE()
    for _ in range(0,4):
        debugprint(dice1, dice_t)
        if (compare(dice1, dice_t)):
            return True
        dice_t.rotateR()

    return False

def debugprint(dice1, dice2, label=''):
    debug=False
    if (debug):
        print(label)
        print('dice1: {}'.format(dice1.label))
        print('dice2: {}'.format(dice2.label))
        print('')

## Main

ndice = int(input())
dices = []
for i in range(0,ndice):
    label = []
    label.append(-1)
    label[1:] = map(int,input().split())
    dice = Dice(label)
    dices.append(dice)

for i in range(0,ndice-1):
    for j in range(i+1, ndice):
        if (verify(dices[i], dices[j])):
            print('No')
            exit()
print('Yes')

