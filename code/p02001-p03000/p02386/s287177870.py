import itertools
import copy

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


def check_1_column(dice1,dice2):
    '''
    input:Diceクラスを2つ読み込む
    output:Dice1を4回縦回転して、Dice2と一致するようであれば1を返す。一致しなければ、0を返す。
    '''
    for b in range(4):
        if dice1.dice[0] == dice2.dice[0] and dice1.dice[1] == dice2.dice[1] and dice1.dice[2] == dice2.dice[2] and dice1.dice[3] == dice2.dice[3] and dice1.dice[4] == dice2.dice[4] and dice1.dice[5] == dice2.dice[5]:
            return 1
        dice1.turn('N')
    return 0

def check_all(dice1,dice2):

    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('N')
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    dice1.turn('E')
    if check_1_column(dice1,dice2):
        return 1
    return 0

# 入力
n = int(input())
input_dice = []
for a in range(n):
    temp = list(map(int,input().split()))
    temp_class = Dice(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5])
    input_dice.append(temp_class)

# Diceを2つ入力
# 一致してたら、Trueを返す。
flag = 0
for a in itertools.combinations(input_dice,2):
    temp1 = copy.copy(a[0])
    temp2 = copy.copy(a[1])
    flag += check_all(temp1,temp2)
if flag == 0:
    print('Yes')
else:
    print('No')

