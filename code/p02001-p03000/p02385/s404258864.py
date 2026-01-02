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
    

x = list(map(int,input().split()))
y = list(map(int,input().split()))

#print(x)
#print(y)

D1 = Dice(x) #generate instance

D2 = Dice(y)
#print(D1.val)
#print(D2.val)

import random 

Determin=False
for i in range(1000):

    D2.rotate(int_to_dir(random.randint(0,4)))
    
    #count+=1
    if D1.val==D2.val:
        #print(D1.val)
        #print(D2.val)
        Determin=True
        #print(i)
    
if Determin:
    print("Yes")
else:
    print("No")
                        
        
