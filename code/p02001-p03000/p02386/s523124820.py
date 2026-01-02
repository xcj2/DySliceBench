class Dice:
    
    def __init__(self, lst):
        self.val=[]
        self.val.append(lst[0])
        self.val.append(lst[1])
        self.val.append(lst[2])
        self.val.append(lst[3])
        self.val.append(lst[4])
        self.val.append(lst[5])

    def rotate(self,dir):
        if dir=="N":
            tmp=self.val[0]
            self.val[0]=self.val[1]
            self.val[1]=self.val[5]
            self.val[5]=self.val[4]
            self.val[4]=tmp
        if dir=="E":
            tmp=self.val[0]
            self.val[0]=self.val[3]
            self.val[3]=self.val[5]
            self.val[5]=self.val[2]
            self.val[2]=tmp
        if dir=="S":
            tmp=self.val[0]
            self.val[0]=self.val[4]
            self.val[4]=self.val[5]
            self.val[5]=self.val[1]
            self.val[1]=tmp
        if dir=="W":
            tmp=self.val[0]
            self.val[0]=self.val[2]
            self.val[2]=self.val[5]
            self.val[5]=self.val[3]
            self.val[3]=tmp

def int_to_dir(n):
    if n==0:
        return "N"
    if n==1:
        return "E"
    if n==2:
        return "S"
    if n==3:
        return "W"

import random 

def areSame(D1,D2):
    Determin=False
    for i in range(100):

        D2.rotate(int_to_dir(random.randint(0,4)))

        if D1.val==D2.val:
            Determin=True

    return Determin
    
    
n = int(input())
Instance=[]
for i in range(n):
    x = list(map(int,input().split()))
    Instance.append(Dice(x))
    #print(Instance)
    #print("val:",Instance[i].val)
    #print(Instace[i].val)

Ans=True
for i in range(n-1):
    for j in range(i+1,n):
        D1=Instance[i]
        D2=Instance[j]
        if areSame(D1,D2):
            Ans=False

if Ans:
    print("Yes")
else:
    print("No")




