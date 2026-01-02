import random

class Dice:
    def __init__(self):
        self.u=1
        self.w=2
        self.s=3
        self.e=4
        self.n=5
        self.d=6
        self.dic={"W":0,"S":1,"E":2,"N":3}
    
    def __init__(self,u,w,s,e,n,d):
        self.u=u
        self.w=w
        self.s=s
        self.e=e
        self.n=n
        self.d=d
        self.dic={"W":0,"S":1,"E":2,"N":3}

    def rot(self,way):
        if isinstance(way,str):
            way=self.dic[way]

        if way==0:
            c=self.u
            self.u=self.e
            self.e=self.d
            self.d=self.w
            self.w=c
        elif way==1:
            c=self.u
            self.u=self.n
            self.n=self.d
            self.d=self.s
            self.s=c
        elif way==2:
            c=self.u
            self.u=self.w
            self.w=self.d
            self.d=self.e
            self.e=c
        else :
            c=self.u
            self.u=self.s
            self.s=self.d
            self.d=self.n
            self.n=c
def dice_check(dice_1,dice_2):
    lst=["W","S"]
    flag=0
    for i in range(100):
        if dice_1.u==dice_2.u and dice_1.w==dice_2.w and dice_1.s==dice_2.s and dice_1.e==dice_2.e and dice_1.n==dice_2.n and dice_1.d==dice_2.d:
            flag=1
        dice_1.rot(random.choice(lst))
    return flag

flag2=0
dices = []
dice_number=int(input())
for i in range(dice_number):
    u,s,e,w,n,d=map(int,input().split())
    dice=Dice(u,w,s,e,n,d)
    dices.append(dice)
for i in range(dice_number):
    for j in range(i+1,dice_number):
        if dice_check(dices[i],dices[j])==1:
            flag2=1
if flag2==0:
    print("Yes")
else:
    print("No")
