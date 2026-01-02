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
 
        if(way==0):
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
    def get_nums(self):   
        return {self.u,self.w,self.s,self.e,self.n,self.w,self.d}

def mk_dice():
    u,s,e,w,n,d=map(int,input().split())
    return Dice(u,w,s,e,n,d)
 
import random
q=int(input())
dice_col=[]
ans=True
for j in range(q):
    dice_b=mk_dice()
    for dice in dice_col:
        if(dice.get_nums()==dice_b.get_nums()):
            for i in range (1000):
                dice.rot(random.randint(0,2))
                if(dice.u==dice_b.u and dice.d==dice_b.d and dice.w==dice_b.w and dice.s==dice_b.s and dice.e==dice_b.e and dice.n==dice_b.n):
                    ans=False
    dice_col.append(dice_b)
 
if ans:
    print('Yes')
else:
    print('No')