from itertools import combinations
class Dice:
    def __init__(self,dim=list(range(1,7))):
        self.dim = dim

    def roll(self,direction):
        if direction == "N":
            buff = self.dim[0]
            self.dim[0] = self.dim[1]
            self.dim[1] = self.dim[5]
            self.dim[5] = self.dim[4]
            self.dim[4] = buff

        if direction == "E":
            buff = self.dim[3]
            self.dim[3] = self.dim[5]
            self.dim[5] = self.dim[2]
            self.dim[2] = self.dim[0]
            self.dim[0] = buff

        if direction == "W":
            buff = self.dim[0]
            self.dim[0] = self.dim[2]
            self.dim[2] = self.dim[5]
            self.dim[5] = self.dim[3]
            self.dim[3] = buff

        if direction == "S":
            buff = self.dim[0]
            self.dim[0] = self.dim[4]
            self.dim[4] = self.dim[5]
            self.dim[5] = self.dim[1]
            self.dim[1] = buff

def dice_ident(lsts,comb):
    for i in comb:
        D1 = Dice(lsts[i[0]])
        D2 = Dice(lsts[i[1]])
        for op in 'EEENEEENEEESEEESEEENEEEN':
            if D1.dim == D2.dim:
                return print("No")
            D1.roll(op)
    return print("Yes")
            

number = int(input())
comb = list(combinations(range(number),2))
lsts = []
for i in range(number):
    lsts.append(list(map(int,input().split())))

dice_ident(lsts,comb)
