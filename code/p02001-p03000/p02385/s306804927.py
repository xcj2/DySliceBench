def North(dice):
    w = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = dice[4]
    dice[4] = w
    return dice
def East(dice):
    w = dice[1]
    dice[1] = dice[2]
    dice[2] = dice[4]
    dice[4] = dice[3]
    dice[3] = w
    return dice

def West(dice):
    w = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = dice[3]
    dice[3] = w
    return dice

maxloop = 4
Ncnt = 0
Ecnt = 0
Wcnt = 0

Dice1 = input().split()
Dice2 = input().split()

Flag = False
Nloop = True
Eloop = True
Wloop = True

while Eloop:
    while Nloop:
        while Wloop:
            if Dice1 == Dice2:
                Flag = True
                Nloop = False
                Eloop = False
                Wloop = False
                break
            Dice1 = West(Dice1)
            Wcnt += 1
            if Wcnt == maxloop:
                Wloop = False
        Dice1 = North(Dice1)
        Wcnt = 0
        Wloop = True
        Ncnt += 1
        if Ncnt == maxloop:
            Nloop = False
    Dice1 = East(Dice1)
    Ncnt = 0
    Nloop = True
    Ecnt += 1
    if Ecnt == maxloop:
        Eloop = False

if Flag == True:
    print("Yes")
else:
    print("No")