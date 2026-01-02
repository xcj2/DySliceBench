from copy import deepcopy

class Dice():

    def num_input(self):
        self.number = list(map(int,input().split()))
        self.E = [4,2,1,6,5,3]
        self.N = [2,6,3,4,1,5]
        self.S = [5,1,3,4,6,2]
        self.W = [3,2,6,1,5,4]
    
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
    
    def output(self):
        print(self.number[0])
    

if __name__ == "__main__":
    dice = Dice()
    dice.num_input()
    order = input()
    for i in order:
        dice.rotate(i)
    dice.output()
