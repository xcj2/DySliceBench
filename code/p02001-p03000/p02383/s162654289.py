def S(dice):
    a_0=dice[0]
    a_1=dice[1]
    a_4=dice[4]
    a_5=dice[5]
    dice[1]=a_0
    dice[5]=a_1
    dice[4]=a_5
    dice[0]=a_4

def N(dice):
    a_0=dice[0]
    a_1=dice[1]
    a_4=dice[4]
    a_5=dice[5]
    dice[1]=a_5
    dice[5]=a_4
    dice[4]=a_0
    dice[0]=a_1

def W(dice):
    a_0=dice[0]
    a_3=dice[3]
    a_5=dice[5]
    a_2=dice[2]
    dice[0]=a_2
    dice[3]=a_0
    dice[5]=a_3
    dice[2]=a_5

def E(dice):
    a_0=dice[0]
    a_3=dice[3]
    a_5=dice[5]
    a_2=dice[2]
    dice[0]=a_3
    dice[3]=a_5
    dice[5]=a_2
    dice[2]=a_0

dice=list(map(int,input().split()))
command=str(input())

for i in command:
    if i=='S':
        S(dice)
    elif i=='N':
        N(dice)
    elif i=='W':
        W(dice)
    elif i=='E':
        E(dice)
print(dice[0])
