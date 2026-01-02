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

n = int(input())
Dice = [['' for i2 in range(6)] for i1 in range(n)]
for i in range(n):
    Dice[i] = input().split()

Flag = False
Nloop = True
Eloop = True
Wloop = True

for i in range(n - 1):
    for j in range(i + 1, n):
        while Eloop:
            while Nloop:
                while Wloop:
                    if Dice[i] == Dice[j]:
                        Flag = True
                        Nloop = False
                        Eloop = False
                        Wloop = False
                        break
                    Dice[i] = West(Dice[i])
                    Wcnt += 1
                    if Wcnt == maxloop:
                        Wloop = False
                Dice[i] = North(Dice[i])
                Wcnt = 0
                Wloop = True
                Ncnt += 1
                if Ncnt == maxloop:
                    Nloop = False
            Dice[i] = East(Dice[i])
            Ncnt = 0
            Nloop = True
            Ecnt += 1
            if Ecnt == maxloop:
                Eloop = False
        Ecnt = 0
        Eloop = True
        if Flag == True:
            print("No")
            break
    else:
        continue
    break

if Flag == False:
    print("Yes")