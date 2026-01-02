class Dice(object):
    def __init__(self,num):
        self.f=num[0]
        self.s=num[1]
        self.e=num[2]
        self.w=num[3]
        self.n=num[4]
        self.b=num[5]
    def create(self,order):
        if order=='N':
            return [self.s,self.b,self.e,self.w,self.f,self.n]
        elif order=='S':
            return [self.n,self.f,self.e,self.w,self.b,self.s]

        elif order=='E':
            return [self.w,self.s,self.f,self.b,self.n,self.e]
        else:
            return [self.e,self.s,self.b,self.f,self.n,self.w]

    @classmethod
    def Dice_create(cls,num):
            return cls(num)
num=list(map(int,input().split()))
q=eval(input())
Q=[]
dice=Dice(num)
T={0:'N',1:'E',2:'S',3:'W'}
for i in range(q):
    Q.append(list(map(int,input().split())))
for i in range(q):
        while True:
            t=[dice.s,dice.w,dice.n,dice.e]
            if dice.f!=Q[i][0]:
                if dice.b!=Q[i][0]:#??´??¢????????¢?????\?????????
                    dice=Dice.Dice_create(dice.create(T[t.index(Q[i][0])]))
                else:#?????¢????????¢?????\?????????
                    dice=Dice.Dice_create(dice.create('N'))
            else:
                print(t[t.index(Q[i][1])-1])#?????¢?????£???????????¢?????\?????????
                break