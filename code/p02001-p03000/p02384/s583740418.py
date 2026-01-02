import random
def N():
    num=Dice[0]
    Dice[0]=Dice[1]
    Dice[1]=Dice[5]
    Dice[5]=Dice[4]
    Dice[4]=num
def E():
    num=Dice[0]
    Dice[0]=Dice[3]
    Dice[3]=Dice[5]
    Dice[5]=Dice[2]
    Dice[2]=num
def W():
    num=Dice[0]
    Dice[0]=Dice[2]
    Dice[2]=Dice[5]
    Dice[5]=Dice[3]
    Dice[3]=num
def S():
    num=Dice[0]
    Dice[0]=Dice[4]
    Dice[4]=Dice[5]
    Dice[5]=Dice[1]
    Dice[1]=num
Dice=[int(i) for i in input().split()]
a=int(input())
for i in range(a):
    x,y=map(int,input().split())
    while True:
        rand=random.randint(1,4)
        if rand==1:
            N()
        elif rand==2:
            E()
        elif rand==3:
            W()
        else:
            S()
        if Dice[0]==x and Dice[1]==y:
            break
    print(Dice[2])