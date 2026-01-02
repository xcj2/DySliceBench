import sys

def swap(dice,i,j,k,l):#diceの目をi→ｊ→ｋ→ｌ→iの順に入れ替える
    x=dice[l]
    dice[l]=dice[k]
    dice[k]=dice[j]
    dice[j]=dice[i]
    dice[i]=x
    return dice

def Sroll(dice):
    dice=swap(dice,0,1,5,4)
    return dice

def Eroll(dice):
    dice=swap(dice,0,2,5,3)
    return dice

def Wroll(dice):
    dice=swap(dice,0,3,5,2)
    return dice

def Nroll(dice):
    dice=swap(dice,0,4,5,1)
    return dice


def judge(dice1,dice2):#2つのダイスが同じなら１を返し、違うなら０を返す
    top=dice1[0]
    fro=dice1[1]

    for j in range(0,8):
        if(fro==dice2[1]):
            break
        if(j==3):
            dice2=Eroll(dice2)
        if(j==7):
            return 0
        dice2=Sroll(dice2)
        
    i=0
    while(top!=dice2[0]):
        dice2=Eroll(dice2)
        if(i==3):
             return 0
        i+=1


    if(dice1[2]==dice2[2] and dice1[3]==dice2[3] and dice1[4]==dice2[4] and dice1[5]==dice2[5]):
        return 1
    else:
        return 0


n=int(input())

if(n==1):
    print("Yes")
    sys.exit()

Dice=[[]]

for i in range(0,n):
    Dice.append(list(map(int,input().split())))
del Dice[0]

for i in range(0,n):
    for j in range(i+1,n):
        if(judge(Dice[i],Dice[j])):
            print("No")
            sys.exit()


print("Yes")
