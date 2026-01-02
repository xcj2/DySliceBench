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
        t = self.label[3]
        self.label[3] = self.label[2]
        self.label[2] = self.label[4]
        self.label[4] = self.label[5]
        self.label[5] = t

    def rotateL(self):
        t = self.label[3]
        self.label[3] = self.label[5]
        self.label[5] = self.label[4]
        self.label[4] = self.label[2]
        self.label[2] = t

def debugprint(dice1, dice2, label=''):
    debug=False
    if (debug):
        print(label)
        print('dice1: {}'.format(dice1.label))
        print('dice2: {}'.format(dice2.label))
        print('')

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


## Main

label1 = []
label1.append(-1)
label1[1:] = map(int,input().split())
dice1 = Dice(label1)
#print(dice1.label)

label2 = []
label2.append(-1)
label2[1:] = map(int,input().split())
dice2 = Dice(label2)
#print(dice2.label)

debugprint(dice1, dice2, 'before rotate')

label1.sort()
label2.sort()
if (label1 != label2):
    print("No")
    exit()

if (verify(dice1, dice2)):
    print('Yes')
else:
    print('No')

