import sys

class Dice:
    def __init__(self,d1,d2,d3,d4,d5,d6):
        self.dice = [d1,d2,d3,d4,d5,d6]
    def turn(self,dir):
        if dir == 'S':
            self.dice = [self.dice[4],self.dice[0],self.dice[2],self.dice[3],self.dice[5],self.dice[1]]
        if dir == 'N':
            self.dice = [self.dice[1],self.dice[5],self.dice[2],self.dice[3],self.dice[0],self.dice[4]]
        if dir == 'W':
            self.dice = [self.dice[2],self.dice[1],self.dice[5],self.dice[0],self.dice[4],self.dice[3]]
        if dir == 'E':
            self.dice = [self.dice[3],self.dice[1],self.dice[0],self.dice[5],self.dice[4],self.dice[2]]


def check(dice1,dice2):
    for b in range(4):
        dice1.turn('N')
        if dice1.dice[0] == dice2.dice[0] and dice1.dice[1] == dice2.dice[1] and dice1.dice[2] == dice2.dice[2] and dice1.dice[3] == dice2.dice[3] and dice1.dice[4] == dice2.dice[4] and dice1.dice[5] == dice2.dice[5]:
            print('Yes')
            sys.exit()

dice1_num = list(map(int,input().split()))
dice2_num = list(map(int,input().split()))
init_Dice1 = Dice(dice1_num[0],dice1_num[1],dice1_num[2],dice1_num[3],dice1_num[4],dice1_num[5])
init_Dice2 = Dice(dice2_num[0],dice2_num[1],dice2_num[2],dice2_num[3],dice2_num[4],dice2_num[5])


check(init_Dice1,init_Dice2)
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
init_Dice2.turn('N')
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
init_Dice2.turn('E')
check(init_Dice1,init_Dice2)
print('No')

