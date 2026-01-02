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
command=input()
dice=Dice(num)
for i in range(len(command)):
    temp=dice.create(command[i])
    dice=Dice.Dice_create(temp)
print(dice.f)