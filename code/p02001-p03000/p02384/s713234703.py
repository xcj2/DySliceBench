class Dice:
    val=[]
    def __init__(self, lst):
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
    

x = list(map(int,input().split()))
q = int(input())

D = Dice(x)

import random 

for i in range(q):
    a,b=map(int,input().split())
    count=0
    while True:
        D.rotate(int_to_dir(random.randint(0,4)))
        #count+=1
        if D.val[0]==a and D.val[1]==b:
            
            print(D.val[2])
            break

