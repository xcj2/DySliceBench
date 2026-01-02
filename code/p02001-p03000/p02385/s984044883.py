class Dice():
    def __init__(self):
        self.number = [i for i in range(6)]
        self.work = [i for i in range(6)]
    def setNumber(self,n0,n1,n2,n3,n4,n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5
    def roll(self,loc):
        for i in range(6):
            self.work[i] = self.number[i]
        if loc == 'E':
            self.setNumber(self.work[3],self.work[1],self.work[0],self.work[5],self.work[4],self.work[2])
        elif loc == 'N':
            self.setNumber(self.work[1],self.work[5],self.work[2],self.work[3],self.work[0],self.work[4])
        elif loc == 'S':
            self.setNumber(self.work[4],self.work[0],self.work[2],self.work[3],self.work[5],self.work[1])
        elif loc == 'W':
            self.setNumber(self.work[2],self.work[1],self.work[5],self.work[0],self.work[4],self.work[3])
dice1 = Dice()
table1 = list(map(int,input().split()))
dice1.setNumber(table1[0], table1[1], table1[2], table1[3], table1[4], table1[5])
dice2 = Dice()
table2 = list(map(int,input().split()))
dice2.setNumber(table2[0], table2[1], table2[2], table2[3], table2[4], table2[5])
for loc in "NNNNWNNNWNNNENNNENNNWNNN":
  dice2.roll(loc)
  if dice2.number==dice1.number:
    print("Yes")
    exit()
print("No")
