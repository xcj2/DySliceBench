from copy import deepcopy

class Dice():

    def __init__(self):
        self.E = [4,2,1,6,5,3]
        self.N = [2,6,3,4,1,5]
        self.S = [5,1,3,4,6,2]
        self.W = [3,2,6,1,5,4]
        self.number = list(map(int,input().split()))
        ##self.order = "NNNNWNNNWNNNENNNENNNWNNN"

    def rotate(self,order):
        tmp = deepcopy(self.number)
        if order == "E":
            for i in range(6):
                self.number[i] = tmp[self.E[i]-1]
        elif order == "N":
            for i in range(6):
                self.number[i] = tmp[self.N[i]-1]
        elif order == "S":
            for i in range(6):
                self.number[i] = tmp[self.S[i]-1]
        elif order == "W":
            for i in range(6):
                self.number[i] = tmp[self.W[i]-1]
    
    def sidenum(self,x,y):
        for i in self.order:
            if self.number[1] == y and self.number[0] == x:
                print(self.number[2])
                break
            else:
                self.rotate(i)
    
    def check(self,other):
        flag = True
        for i in range(6):
            if self.number[i] != other.number[i]:
                flag = False
        return flag

if __name__ == "__main__":
    flag = False
    dice1 = Dice()
    dice2 = Dice()
    order = "NNNNWNNNWNNNENNNENNNWNNN"
    for i in order:
        dice1.rotate(i)
        if dice1.check(dice2):
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")
