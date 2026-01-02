def N(Dice):
    num=Dice[0]
    Dice[0]=Dice[1]
    Dice[1]=Dice[5]
    Dice[5]=Dice[4]
    Dice[4]=num
def E(Dice):
    num=Dice[0]
    Dice[0]=Dice[3]
    Dice[3]=Dice[5]
    Dice[5]=Dice[2]
    Dice[2]=num
def W(Dice):
    num=Dice[0]
    Dice[0]=Dice[2]
    Dice[2]=Dice[5]
    Dice[5]=Dice[3]
    Dice[3]=num
def S(Dice):
    num=Dice[0]
    Dice[0]=Dice[4]
    Dice[4]=Dice[5]
    Dice[5]=Dice[1]
    Dice[1]=num
def DICE(Dice,Dice2):
    if (Dice[0] in Dice2)==False:
        """print('No')"""
        return 0
    else:
        for j in range(6):
            if j%2==0:
                N(Dice2)
            else:
                W(Dice2)
            for i in range(4):
                N(Dice2)
                W(Dice2)
                S(Dice2)
                if Dice==Dice2:
                    break
            if Dice==Dice2:
                break
    if Dice==Dice2:
        """print('Yes')"""
        return 1
    else:
        """print('No')"""
        return 0
cnt=0             
a=int(input())
Dice=[i for i in range(a)]
for i in range(a):
     Dice[i]=[int(i) for i in input().split()]
for i in range(a-1):
    for j in range(i+1,a):
        cnt+=DICE(Dice[i],Dice[j])
if cnt==0:
    print("Yes")
else:
    print("No")
        