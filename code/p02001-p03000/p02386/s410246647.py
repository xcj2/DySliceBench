from copy import deepcopy

class Dice():

    def __init__(self):
        self.E = [4,2,1,6,5,3]
        self.N = [2,6,3,4,1,5]
        self.S = [5,1,3,4,6,2]
        self.W = [3,2,6,1,5,4]
        self.number = list(map(int,input().split()))
        self.order = "NNNNWNNNWNNNENNNENNNWNNN"

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
        flag = False
        for i in self.order:
            self.rotate(i)
            if self.number == other.number:
                flag = True
                break
        return flag

if __name__ == "__main__":
    n = int(input())
    dices = []
    for i in range(n):
        tmp = Dice()
        dices.append(tmp)
    flag = True
    for i in range(n-1):
        for j in range(i+1,n):
            if dices[i].check(dices[j]):
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
