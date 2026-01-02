import sys

class Dise():
    def __init__(self, aLabelList):
        self.LabelList = aLabelList
        self.NEWS = {"N": [0,4,5,1],
                     "E": [0,2,5,3],
                     "W": [0,3,5,2],
                     "S": [0,1,5,4],
                     "R": [1,2,4,3]}
       
    def move(self,aNEWS):
        idx = self.NEWS[aNEWS]
        tmp = self.LabelList[idx[0]]
        self.LabelList[idx[0]] = self.LabelList[idx[3]]
        self.LabelList[idx[3]] = self.LabelList[idx[2]]
        self.LabelList[idx[2]] = self.LabelList[idx[1]]
        self.LabelList[idx[1]] = tmp

def step1():
    for i in range(4):
        if Dise1.LabelList[0] == Dise2.LabelList[0] and \
           Dise1.LabelList[5] == Dise2.LabelList[5]:
            step2()
        else:
            Dise2.move("E")
    
    Dise2.move("N")
    if Dise1.LabelList[0] == Dise2.LabelList[0] and \
       Dise1.LabelList[5] == Dise2.LabelList[5]:
        step2()
    
    Dise2.move("S")
    Dise2.move("S")
    if Dise1.LabelList[0] == Dise2.LabelList[0] and \
       Dise1.LabelList[5] == Dise2.LabelList[5]:
        step2()
    
def step2():
    for i in range(4):
        if Dise1.LabelList[1] == Dise2.LabelList[1] and \
           Dise1.LabelList[2] == Dise2.LabelList[2] and \
           Dise1.LabelList[3] == Dise2.LabelList[3] and \
           Dise1.LabelList[4] == Dise2.LabelList[4]:
            print("No")
            sys.exit()
        else:
            Dise2.move("R")

n = int(input())
DiseList = [Dise(input().split()) for i in range(n)]
for x in range(n-1):
    for y in range(x+1,n):
        Dise1 = DiseList[x]
        Dise2 = DiseList[y]
        step1()

print("Yes")


