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




dice1=list(map(int,input().split()))
dice2=list(map(int,input().split()))

top=dice1[0]
fro=dice1[1]

for j in range(0,8):
    if(fro==dice2[1]):
        break
    if(j==3):
        dice2=Eroll(dice2)
    dice2=Sroll(dice2)
while(top!=dice2[0]):
    dice2=Eroll(dice2)

if(dice1[2]==dice2[2]):
    print("Yes")
else:
    print("No")
