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




dice=list(map(int,input().split()))
n=int(input())
for i in range(0,n):
    top,fro=map(int,input().split())
    for j in range(0,8):
        if(fro==dice[1]):
            break
        if(j==3):
            dice=Eroll(dice)
        dice=Sroll(dice)
    while(top!=dice[0]):
        dice=Eroll(dice)
    print(dice[2])
