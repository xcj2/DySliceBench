class Dice:
        def __init__(self, strList):
                self.label = strList[:]
                self.label[0] = int(self.label[0])
                self.label[1] = int(self.label[1])
                self.label[2] = int(self.label[2])
                self.label[3] = int(self.label[3])
                self.label[4] = int(self.label[4])
                self.label[5] = int(self.label[5])
        def reset(self, strList):
                self.label = strList[:]
                self.label[0] = int(self.label[0])
                self.label[1] = int(self.label[1])
                self.label[2] = int(self.label[2])
                self.label[3] = int(self.label[3])
                self.label[4] = int(self.label[4])
                self.label[5] = int(self.label[5])
        def rollE(self):
                temp = self.label[3]
                self.label[3] = self.label[5]
                self.label[5] = self.label[2]
                self.label[2] = self.label[0]
                self.label[0] = temp
        def rollN(self):
                temp = self.label[0]
                self.label[0] = self.label[1]
                self.label[1] = self.label[5]
                self.label[5] = self.label[4]
                self.label[4] = temp
        def rollA(self):
                temp = self.label[3]
                self.label[3] = self.label[4]
                self.label[4] = self.label[2]
                self.label[2] = self.label[1]
                self.label[1] = temp
        def printDice(self):
                print(self.label)

def check(d1, d2):
        for i in range(6):
                if d1.label[i] != d2.label[i]:
                        return False
        return True
        
num = int(input())
diceList = []

for i in range(num):
        diceList.append(Dice(input().split()))

isSame = False

for a in range(num):
        for b in range(a + 1, num):
                for j in range(6):
                        for k in range(4):
                                diceList[a].rollA()
                                if check(diceList[a], diceList[b]):
                                        isSame = True
                                        break
                        if j % 2 == 0:
                                diceList[a].rollE()
                        else:
                                diceList[a].rollN()
                        if isSame:
                                break
                if isSame:
                        break
        if isSame:
                break

if isSame:
        print('No')
else:
        print('Yes')
