import sys
class Dice:
    def __init__(self,a):
        self.dice = [0 for i in range(len(a))]
        for i in range(len(a)):
            self.dice[i] = a[i]

    def N(self):
        self.dice[0],self.dice[1],self.dice[4],self.dice[5] = self.dice[1],self.dice[5],self.dice[0],self.dice[4]

    def S(self):
        self.dice[0],self.dice[1],self.dice[4],self.dice[5] = self.dice[4],self.dice[0],self.dice[5],self.dice[1]

    def E(self):
        self.dice[0],self.dice[2],self.dice[3],self.dice[5] = self.dice[3],self.dice[0],self.dice[5],self.dice[2]

    def W(self):
        self.dice[0],self.dice[2],self.dice[3],self.dice[5] = self.dice[2],self.dice[5],self.dice[0],self.dice[3]

    def R(self):
        self.dice[1],self.dice[2],self.dice[3],self.dice[4] = self.dice[3],self.dice[1],self.dice[4],self.dice[2]

    def L(self):
        self.dice[1],self.dice[2],self.dice[3],self.dice[4] = self.dice[2],self.dice[4],self.dice[1],self.dice[3]

    #確認用
    def output(self):
        print(self.dice)

def comparison(dice1,dice2):
    dir = 'RRRRNRRRRSWRRRREERRRRWSRRRRNNNRRRR'
    for c in dir:
        if c == "R":
            dice1.R()
        elif c == "N":
            dice1.N()
        elif c == "S":
            dice1.S()
        elif c == "W":
            dice1.W()
        elif c == "E":
            dice1.E()
        elif c == "L":
            dice1.L()
        if dice1.dice == dice2.dice:
            return True
    if dice1.dice != dice2.dice:
        return False

n = int(input())
dice_list = []
Judge = []

for i in range(n):
    a = [int(i) for i in input().split()]
    dice = Dice(a)
    dice_list.append(dice)
for i in range(n-1):
    for j in range(i+1,n):
        if comparison(dice_list[i],dice_list[j]) == True:
            print("No")
            sys.exit()
        else:
            Judge.append(comparison(dice_list[i],dice_list[j]))

print('Yes')

