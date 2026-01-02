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


def check(m):
    for b in range(4):
        m.turn('N')
        if m.dice[0] == a[0] and m.dice[1] == a[1]:
            return(m.dice[2])

dice_num = input().split()
q = int(input())
conditions = []
for a in range(q):
    temp = input().split()
    conditions.append(temp)

init_Dice = Dice(dice_num[0],dice_num[1],dice_num[2],dice_num[3],dice_num[4],dice_num[5])

kaitou = []
for a in conditions:
    if check(init_Dice):
        print(check(init_Dice))
        continue
    init_Dice.turn('E')
    if check(init_Dice):
        print(check(init_Dice))
        continue
    init_Dice.turn('E')
    if check(init_Dice):
        print(check(init_Dice))
        continue
    init_Dice.turn('E')
    if check(init_Dice):
        print(check(init_Dice))
        continue

    init_Dice.turn('W')
    init_Dice.turn('N')
    init_Dice.turn('E')

    if check(init_Dice):
        print(check(init_Dice))
        continue
    init_Dice.turn('E')
    if check(init_Dice):
        print(check(init_Dice))
        continue
    init_Dice.turn('E')
    if check(init_Dice):
        print(check(init_Dice))
        continue
    init_Dice.turn('E')
    if check(init_Dice):
        print(check(init_Dice))
        continue

